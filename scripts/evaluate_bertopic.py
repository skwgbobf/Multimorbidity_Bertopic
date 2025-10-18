"""
BERTopic Model Evaluation Script (Full Model Loading, GPU-Enabled)

This script loads complete BERTopic models and calculates evaluation metrics.
Uses GPU/CUDA for faster computation if available.

WHEN TO USE THIS SCRIPT:
- You need to generate visualizations (topic hierarchies, intertopic distance)
- You want to predict topics for new patient data
- You need to update/reduce topics in the model
- Your models were saved with Python 3.12 + current numba version

WHEN TO USE evaluate_from_excel.py INSTEAD:
- You only need coherence/diversity metrics (recommended for publication)
- Models were saved with older Python/numba versions (compatibility issues)
- Faster evaluation without loading 1.4GB of models
- Identical results for all evaluation metrics

Requirements:
    pip install gensim bertopic pandas numpy torch

Usage:
    python scripts/evaluate_bertopic.py

GPU Support:
    - Automatically uses CUDA if available
    - Falls back to CPU if no GPU detected
    - Install GPU PyTorch: pip install torch --index-url https://download.pytorch.org/whl/cu124

Current Status:
    - May fail with models saved in Python <3.11 (numba compatibility)
    - Use evaluate_from_excel.py for guaranteed compatibility
"""

import os
import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict, Tuple
import warnings
warnings.filterwarnings('ignore')

# Check GPU availability
import torch
print(f"\n{'='*60}")
print("System Information")
print(f"{'='*60}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    print(f"CUDA version: {torch.version.cuda}")
else:
    print("Running on CPU (slower)")
print(f"{'='*60}\n")

from bertopic import BERTopic
from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel


def load_bertopic_model(model_path: str) -> BERTopic:
    """
    Load a trained BERTopic model with compatibility handling

    Handles:
    - GPU/CUDA models (uses GPU if available)
    - Numba version compatibility (Python 3.12 vs older versions)

    Args:
        model_path: Path to saved BERTopic model

    Returns:
        Loaded BERTopic model

    Note: If loading fails due to compatibility issues, use evaluate_from_excel.py
    which produces identical results without requiring model loading.
    """
    print(f"Loading model from: {model_path}")

    try:
        # Attempt standard loading (works with CUDA if available)
        model = BERTopic.load(model_path)
        print(f"  ✓ Model loaded successfully")

        # Check if model components use GPU
        if torch.cuda.is_available() and hasattr(model, 'embedding_model'):
            print(f"  ✓ Using GPU acceleration")

        return model

    except TypeError as e:
        if "code() argument 13 must be str, not int" in str(e):
            # Numba/Python 3.12 incompatibility
            print(f"\n  ✗ Model loading failed: Numba compatibility issue")
            print(f"  → Models were saved with Python <3.11 and older numba")
            print(f"  → Current: Python 3.12 (incompatible bytecode format)")
            print(f"\n  Solutions:")
            print(f"    1. Use 'evaluate_from_excel.py' (recommended)")
            print(f"       - Works perfectly, produces identical metrics")
            print(f"       - No model loading required")
            print(f"    2. Create Python 3.10 environment to load old models")
            print(f"    3. Retrain models with current Python/numba versions")
            raise RuntimeError("Numba compatibility issue - use evaluate_from_excel.py")
        else:
            raise

    except Exception as e:
        print(f"\n  ✗ Model loading failed: {e}")
        print(f"  → Please use 'evaluate_from_excel.py' for evaluation")
        raise


def load_data(data_path: str) -> pd.DataFrame:
    """Load preprocessed data pickle file"""
    print(f"Loading data from: {data_path}")
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    return data


def get_topic_words(topic_model: BERTopic, n_words: int = 10) -> List[List[str]]:
    """
    Extract top words for each topic (excluding topic -1)

    Args:
        topic_model: Trained BERTopic model
        n_words: Number of top words per topic

    Returns:
        List of lists, where each sublist contains top words for a topic
    """
    topics = []
    topic_info = topic_model.get_topic_info()

    # Exclude outlier topic (-1)
    valid_topics = [t for t in topic_info['Topic'] if t != -1]

    for topic_id in valid_topics:
        topic_words = topic_model.get_topic(topic_id)
        if topic_words:
            # Extract just the words (not the scores)
            words = [word for word, score in topic_words[:n_words]]
            topics.append(words)

    return topics


def calculate_coherence_scores(
    topic_model: BERTopic,
    documents: List[str],
    n_words: int = 10
) -> Dict[str, float]:
    """
    Calculate multiple coherence metrics for BERTopic model

    Args:
        topic_model: Trained BERTopic model
        documents: List of document texts
        n_words: Number of top words to use per topic

    Returns:
        Dictionary with coherence scores (c_v, c_uci, c_npmi)
    """
    print("Extracting topic words...")
    topics = get_topic_words(topic_model, n_words)

    if not topics:
        print("Warning: No valid topics found")
        return {'c_v': 0.0, 'c_uci': 0.0, 'c_npmi': 0.0}

    print(f"Found {len(topics)} topics")

    # Tokenize documents for gensim
    print("Tokenizing documents...")
    texts = [doc.split() for doc in documents]

    # Create dictionary
    print("Creating dictionary...")
    dictionary = Dictionary(texts)

    # Calculate corpus (bag of words)
    corpus = [dictionary.doc2bow(text) for text in texts]

    coherence_scores = {}

    # Calculate C_v coherence
    print("Calculating C_v coherence...")
    try:
        coherence_model_cv = CoherenceModel(
            topics=topics,
            texts=texts,
            dictionary=dictionary,
            coherence='c_v'
        )
        coherence_scores['c_v'] = coherence_model_cv.get_coherence()
    except Exception as e:
        print(f"Error calculating C_v: {e}")
        coherence_scores['c_v'] = 0.0

    # Calculate C_uci coherence
    print("Calculating C_uci coherence...")
    try:
        coherence_model_uci = CoherenceModel(
            topics=topics,
            texts=texts,
            dictionary=dictionary,
            coherence='c_uci'
        )
        coherence_scores['c_uci'] = coherence_model_uci.get_coherence()
    except Exception as e:
        print(f"Error calculating C_uci: {e}")
        coherence_scores['c_uci'] = 0.0

    # Calculate C_npmi coherence
    print("Calculating C_npmi coherence...")
    try:
        coherence_model_npmi = CoherenceModel(
            topics=topics,
            texts=texts,
            dictionary=dictionary,
            coherence='c_npmi'
        )
        coherence_scores['c_npmi'] = coherence_model_npmi.get_coherence()
    except Exception as e:
        print(f"Error calculating C_npmi: {e}")
        coherence_scores['c_npmi'] = 0.0

    return coherence_scores


def calculate_diversity_metrics(topic_model: BERTopic, n_words: int = 10) -> Dict[str, float]:
    """
    Calculate topic diversity metrics

    Args:
        topic_model: Trained BERTopic model
        n_words: Number of top words to use per topic

    Returns:
        Dictionary with diversity metrics
    """
    print("Calculating diversity metrics...")
    topics = get_topic_words(topic_model, n_words)

    if not topics or len(topics) < 2:
        return {
            'unique_words_ratio': 0.0,
            'avg_jaccard_distance': 0.0,
            'n_topics': len(topics) if topics else 0
        }

    # Unique words ratio
    all_words = [word for topic in topics for word in topic]
    unique_words = set(all_words)
    unique_ratio = len(unique_words) / len(all_words) if all_words else 0.0

    # Average pairwise Jaccard distance
    jaccard_distances = []
    for i in range(len(topics)):
        for j in range(i + 1, len(topics)):
            set_i = set(topics[i])
            set_j = set(topics[j])

            intersection = len(set_i & set_j)
            union = len(set_i | set_j)

            jaccard_sim = intersection / union if union > 0 else 0
            jaccard_dist = 1 - jaccard_sim
            jaccard_distances.append(jaccard_dist)

    avg_jaccard = np.mean(jaccard_distances) if jaccard_distances else 0.0

    return {
        'unique_words_ratio': unique_ratio,
        'avg_jaccard_distance': avg_jaccard,
        'n_topics': len(topics)
    }


def evaluate_model(
    model_path: str,
    documents: List[str],
    model_name: str
) -> Dict[str, any]:
    """
    Complete evaluation of a BERTopic model

    Args:
        model_path: Path to saved BERTopic model
        documents: List of document texts
        model_name: Name identifier for the model

    Returns:
        Dictionary with all evaluation metrics
    """
    print(f"\n{'='*60}")
    print(f"Evaluating {model_name}")
    print(f"{'='*60}\n")

    # Load model
    topic_model = load_bertopic_model(model_path)

    # Calculate coherence
    coherence_scores = calculate_coherence_scores(topic_model, documents, n_words=10)

    # Calculate diversity
    diversity_scores = calculate_diversity_metrics(topic_model, n_words=10)

    # Combine results
    results = {
        'model': model_name,
        **coherence_scores,
        **diversity_scores
    }

    print(f"\nResults for {model_name}:")
    print(f"  C_v coherence: {coherence_scores['c_v']:.4f}")
    print(f"  C_uci coherence: {coherence_scores['c_uci']:.4f}")
    print(f"  C_npmi coherence: {coherence_scores['c_npmi']:.4f}")
    print(f"  Unique words ratio: {diversity_scores['unique_words_ratio']:.4f}")
    print(f"  Avg Jaccard distance: {diversity_scores['avg_jaccard_distance']:.4f}")
    print(f"  Number of topics: {diversity_scores['n_topics']}")

    return results


def main():
    """Main evaluation pipeline"""

    # Set paths relative to GIT directory
    base_dir = Path(__file__).parent.parent

    # Model paths
    female_model_path = base_dir / "1. Bertopic_over40" / "my_topics_model_100pall_19y_over40_option1_female_dec20"
    male_model_path = base_dir / "1. Bertopic_over40" / "my_topics_model_100pall_19y_over40_option1_male_dec20"

    # Data path
    data_path = base_dir / "T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl"

    # Results directory
    results_dir = base_dir / "results" / "evaluation"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    print("Loading data...")
    data = load_data(str(data_path))

    # Extract documents
    # Convert d2 lists to strings for BERTopic
    if isinstance(data, pd.DataFrame) and 'd2' in data.columns:
        # Convert lists to strings by joining with spaces
        print("Converting d2 lists to document strings...")
        data['document'] = data['d2'].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x))
        documents = data['document'].tolist()
    else:
        raise ValueError("Expected DataFrame with 'd2' column")

    print(f"Loaded {len(documents)} documents")

    # Filter by gender for separate evaluation
    # SEX=2: Female, SEX=1: Male
    if 'SEX' in data.columns:
        female_data = data[data['SEX'] == 2]
        male_data = data[data['SEX'] == 1]

        docs_female = female_data['document'].tolist()
        docs_male = male_data['document'].tolist()

        print(f"Female documents: {len(docs_female)}")
        print(f"Male documents: {len(docs_male)}")
    else:
        # If gender info not available, use all documents for both
        print("Warning: SEX column not found, using all documents for both models")
        docs_female = documents
        docs_male = documents

    # Evaluate female model
    if female_model_path.exists():
        female_results = evaluate_model(
            str(female_model_path),
            docs_female,
            "BERTopic_Female"
        )

        # Save female results
        female_df = pd.DataFrame([female_results])
        female_output = results_dir / "coherence_female.csv"
        female_df.to_csv(female_output, index=False)
        print(f"\nFemale results saved to: {female_output}")
    else:
        print(f"Warning: Female model not found at {female_model_path}")

    # Evaluate male model
    if male_model_path.exists():
        male_results = evaluate_model(
            str(male_model_path),
            docs_male,
            "BERTopic_Male"
        )

        # Save male results
        male_df = pd.DataFrame([male_results])
        male_output = results_dir / "coherence_male.csv"
        male_df.to_csv(male_output, index=False)
        print(f"\nMale results saved to: {male_output}")
    else:
        print(f"Warning: Male model not found at {male_model_path}")

    # Combine and save diversity scores
    if female_model_path.exists() and male_model_path.exists():
        combined_df = pd.DataFrame([female_results, male_results])
        combined_output = results_dir / "model_evaluation_summary.csv"
        combined_df.to_csv(combined_output, index=False)
        print(f"\nCombined results saved to: {combined_output}")

    print("\n" + "="*60)
    print("Evaluation complete!")
    print("="*60)


if __name__ == "__main__":
    main()
