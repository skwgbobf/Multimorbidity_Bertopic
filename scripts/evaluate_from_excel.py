"""
BERTopic Model Evaluation from Saved Excel Files
Calculates coherence and diversity metrics WITHOUT loading the full model
(Workaround for numba/pickle compatibility issues)

Requirements:
    pip install gensim pandas numpy openpyxl

Usage:
    python scripts/evaluate_from_excel.py
"""

import pickle
import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Dict
import warnings
warnings.filterwarnings('ignore')

from gensim.corpora import Dictionary
from gensim.models.coherencemodel import CoherenceModel


def load_data(data_path: str) -> pd.DataFrame:
    """Load preprocessed data pickle file"""
    print(f"Loading data from: {data_path}")
    with open(data_path, 'rb') as f:
        data = pickle.load(f)
    return data


def load_topics_from_excel(excel_path: str, top_n_words: int = 10) -> List[List[str]]:
    """
    Extract topic words from BERTopic's saved Excel file

    Args:
        excel_path: Path to topics_info Excel file
        top_n_words: Number of top words to extract per topic

    Returns:
        List of lists, where each sublist contains top words for a topic
    """
    print(f"Loading topics from: {excel_path}")

    # Load the topics_info Excel file
    df = pd.read_excel(excel_path)

    # The Excel file has columns: Topic, Count, Name, Representation, ...
    # The Representation column contains the disease codes as strings like "['218', '220', ...]"

    topics = []

    # Parse Representation column
    for _, row in df.iterrows():
        if row['Topic'] == -1:  # Skip outlier topic
            continue

        # Representation is a string like "['218', '220', '124', ...]"
        rep = row['Representation']

        if isinstance(rep, str):
            # Parse string representation of list
            try:
                import ast
                words_list = ast.literal_eval(rep)
                if isinstance(words_list, list):
                    # words_list might be simple list ['218', '220'] or tuples [('218', 0.5), ('220', 0.4)]
                    words = []
                    for item in words_list[:top_n_words]:
                        if isinstance(item, (tuple, list)):
                            words.append(str(item[0]))  # Take first element (word/code)
                        else:
                            words.append(str(item))
                else:
                    # If not a list, just split
                    words = str(rep).split()[:top_n_words]
            except (ValueError, SyntaxError):
                # If parsing fails, try manual parsing
                words = str(rep).replace('[', '').replace(']', '').replace("'", "").replace('"', '').split(',')[:top_n_words]
                words = [w.strip() for w in words if w.strip()]
        else:
            # If not a string, convert to string and split
            words = str(rep).split()[:top_n_words]

        if words:
            topics.append(words)

    print(f"Extracted {len(topics)} topics (excluding outlier topic -1)")
    return topics


def calculate_coherence_scores(
    topics: List[List[str]],
    documents: List[str]
) -> Dict[str, float]:
    """
    Calculate multiple coherence metrics

    Args:
        topics: List of topic word lists
        documents: List of document texts

    Returns:
        Dictionary with coherence scores (c_v, c_uci, c_npmi)
    """
    if not topics:
        print("Warning: No valid topics found")
        return {'c_v': 0.0, 'c_uci': 0.0, 'c_npmi': 0.0}

    print(f"Calculating coherence for {len(topics)} topics...")

    # Tokenize documents for gensim
    print("Tokenizing documents...")
    texts = [doc.split() for doc in documents]

    # Create dictionary
    print("Creating dictionary...")
    dictionary = Dictionary(texts)

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


def calculate_diversity_metrics(topics: List[List[str]]) -> Dict[str, float]:
    """
    Calculate topic diversity metrics

    Args:
        topics: List of topic word lists

    Returns:
        Dictionary with diversity metrics
    """
    print("Calculating diversity metrics...")

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


def main():
    """Main evaluation pipeline"""

    # Set paths relative to GIT directory
    base_dir = Path(__file__).parent.parent

    # Excel file paths (saved topic information)
    female_excel = base_dir / "1. Bertopic_over40" / "topics_info_100p_over40_op1_female_dec20.xlsx"
    male_excel = base_dir / "1. Bertopic_over40" / "topics_info_100p_over40_op1_male_dec20.xlsx"

    # Data path
    data_path = base_dir / "T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl"

    # Results directory
    results_dir = base_dir / "results" / "evaluation"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    print("\n" + "="*60)
    print("Loading data...")
    print("="*60 + "\n")

    data = load_data(str(data_path))

    # Extract and convert documents
    if isinstance(data, pd.DataFrame) and 'd2' in data.columns:
        print("Converting d2 lists to document strings...")
        data['document'] = data['d2'].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x))
        documents = data['document'].tolist()
    else:
        raise ValueError("Expected DataFrame with 'd2' column")

    print(f"Loaded {len(documents)} documents")

    # Filter by gender
    if 'SEX' in data.columns:
        female_data = data[data['SEX'] == 2]
        male_data = data[data['SEX'] == 1]

        docs_female = female_data['document'].tolist()
        docs_male = male_data['document'].tolist()

        print(f"Female documents: {len(docs_female)}")
        print(f"Male documents: {len(docs_male)}")
    else:
        print("Warning: SEX column not found")
        docs_female = documents
        docs_male = documents

    # Evaluate female model
    if female_excel.exists():
        print("\n" + "="*60)
        print("Evaluating Female Model")
        print("="*60 + "\n")

        female_topics = load_topics_from_excel(str(female_excel), top_n_words=10)
        female_coherence = calculate_coherence_scores(female_topics, docs_female)
        female_diversity = calculate_diversity_metrics(female_topics)

        female_results = {
            'model': 'BERTopic_Female',
            **female_coherence,
            **female_diversity
        }

        print(f"\nResults for Female Model:")
        print(f"  C_v coherence: {female_coherence['c_v']:.4f}")
        print(f"  C_uci coherence: {female_coherence['c_uci']:.4f}")
        print(f"  C_npmi coherence: {female_coherence['c_npmi']:.4f}")
        print(f"  Unique words ratio: {female_diversity['unique_words_ratio']:.4f}")
        print(f"  Avg Jaccard distance: {female_diversity['avg_jaccard_distance']:.4f}")
        print(f"  Number of topics: {female_diversity['n_topics']}")

        # Save results
        female_df = pd.DataFrame([female_results])
        female_output = results_dir / "coherence_female.csv"
        female_df.to_csv(female_output, index=False)
        print(f"\nSaved to: {female_output}")
    else:
        print(f"Warning: Female Excel file not found at {female_excel}")
        female_results = None

    # Evaluate male model
    if male_excel.exists():
        print("\n" + "="*60)
        print("Evaluating Male Model")
        print("="*60 + "\n")

        male_topics = load_topics_from_excel(str(male_excel), top_n_words=10)
        male_coherence = calculate_coherence_scores(male_topics, docs_male)
        male_diversity = calculate_diversity_metrics(male_topics)

        male_results = {
            'model': 'BERTopic_Male',
            **male_coherence,
            **male_diversity
        }

        print(f"\nResults for Male Model:")
        print(f"  C_v coherence: {male_coherence['c_v']:.4f}")
        print(f"  C_uci coherence: {male_coherence['c_uci']:.4f}")
        print(f"  C_npmi coherence: {male_coherence['c_npmi']:.4f}")
        print(f"  Unique words ratio: {male_diversity['unique_words_ratio']:.4f}")
        print(f"  Avg Jaccard distance: {male_diversity['avg_jaccard_distance']:.4f}")
        print(f"  Number of topics: {male_diversity['n_topics']}")

        # Save results
        male_df = pd.DataFrame([male_results])
        male_output = results_dir / "coherence_male.csv"
        male_df.to_csv(male_output, index=False)
        print(f"\nSaved to: {male_output}")
    else:
        print(f"Warning: Male Excel file not found at {male_excel}")
        male_results = None

    # Combine results
    if female_results and male_results:
        combined_df = pd.DataFrame([female_results, male_results])
        combined_output = results_dir / "model_evaluation_summary.csv"
        combined_df.to_csv(combined_output, index=False)
        print(f"\nCombined results saved to: {combined_output}")

    print("\n" + "="*60)
    print("Evaluation Complete!")
    print("="*60)


if __name__ == "__main__":
    main()
