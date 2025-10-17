# Usage Guide: Multimorbidity Analysis using BERTopic

This guide provides step-by-step instructions for using the codebase to preprocess data and perform BERTopic analysis on multimorbidity patterns.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Data Preparation](#data-preparation)
4. [Workflow Overview](#workflow-overview)
5. [Step 1: Data Preprocessing](#step-1-data-preprocessing)
6. [Step 2: BERTopic Analysis](#step-2-bertopic-analysis)
7. [Understanding the Results](#understanding-the-results)
8. [Troubleshooting](#troubleshooting)
9. [Advanced Usage](#advanced-usage)

## Prerequisites

### System Requirements
- **RAM**: 16GB minimum (32GB recommended)
- **Storage**: 10GB free space
- **OS**: Windows, Linux, or macOS
- **Python**: 3.7 or higher

### Required Knowledge
- Basic Python programming
- Familiarity with Jupyter Notebooks
- Understanding of pandas DataFrames
- Basic knowledge of EHR data structures

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Multimorbidity_Bertopic.git
cd Multimorbidity_Bertopic
```

### 2. Set Up Python Environment

**Option A: Using venv**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**Option B: Using conda**
```bash
conda create -n multimorbidity python=3.8
conda activate multimorbidity
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
jupyter>=1.0.0
notebook>=6.4.0
bertopic>=0.12.0
scikit-learn>=0.24.0
openpyxl>=3.0.0  # For Excel file handling
pickle5>=0.0.11  # For Python < 3.8
scipy>=1.7.0
```

## Data Preparation

### Initial Data Files (Required)

Before running the preprocessing notebooks, you need these CSV files:

1. **DS.csv** - Disease code definitions
   - Columns: `d`, `dname`, `wash_out`

2. **T20.csv** - Disease occurrence records
   - Columns: `YEAR`, `ID`, `d`

3. **BFC.csv** - Patient demographics
   - Columns: `ID`, `SEX`, `AGE`, `GAIBJA`

**Place these files in a known directory** (referenced in notebooks as `csv_dir`).

### File Locations

Update the `csv_dir` variable in the preprocessing notebooks:

```python
# In the notebook, find this line and update the path:
csv_dir = '/path/to/your/csv/files/'
```

## Workflow Overview

```
Step 1: Data Preprocessing
    ├── Load CSV files
    ├── Filter patients aged 40+
    ├── Create temporal sequences
    └── Export preprocessed pickle files
         ↓
Step 2: BERTopic Analysis
    ├── Load preprocessed data
    ├── Stratify by gender
    ├── Train BERTopic models
    └── Export results
```

## Step 1: Data Preprocessing

### Using the Simplified Notebook (Recommended for First-Time Users)

**File:** `SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb`

#### 1.1 Launch Jupyter Notebook

```bash
jupyter notebook
```

Navigate to and open: `SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb`

#### 1.2 Configure Data Paths

In the notebook, find and update this cell:

```python
csv_dir = '/home/skbae/Desktop/146/cancer_conquerance/Work/Mar2023/test_data/'
```

Change to your data directory:

```python
csv_dir = 'C:/Data/your_data_folder/'  # Windows
# or
csv_dir = '/home/username/data/'  # Linux/Mac
```

#### 1.3 Run Preprocessing Cells

Execute cells sequentially (Shift+Enter) through these sections:

**Section 1: Import Data**
```python
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# This section loads CSV files
Dis_codeF = pd.read_csv(csv_dir + "DS.csv")
T20 = pd.read_csv(csv_dir + "T20.csv")
BFC = pd.read_csv(csv_dir + "BFC.csv")
```

**Section 2: Convert to Pickle**
```python
# Saves data as pickle files for faster loading
with open('DS.pkl', 'wb') as f:
    pickle.dump(Dis_codeF, f)

with open('T20.pkl', 'wb') as f:
    pickle.dump(T20, f)

with open('BFC.pkl', 'wb') as f:
    pickle.dump(BFC, f)
```

**Section 3: Filter Age 40+**
```python
# Merge disease records with demographics
T20_BFC = pd.merge(T20, BFC, how='left', on='ID')

# Filter patients aged 40 and above
T20_BFC_over40 = T20_BFC.loc[T20_BFC['AGE'] > 39]
print(f"Patients over 40: {len(T20_BFC_over40)}")
```

**Section 4: Create Age Sequences**
```python
# Calculate age at each disease occurrence
T20_BFC_over40['AGE2'] = T20_BFC_over40['YEAR'].astype('int64') - 2002 + T20_BFC_over40['AGE'].astype('int64')
```

**Section 5: Create Temporal Sequences**
```python
# Group diseases by patient and year, add SEP separators
grouped_diagnoses2 = T20_BFC_over40.groupby(['ID','YEAR'])[['d', 'AGE2']].agg(list).reset_index()
grouped_diagnoses2['d2'] = grouped_diagnoses2['d'].apply(lambda x: x + ['SEP'])
# ... (continue with notebook cells)
```

**Section 6: Export Processed Data**
```python
# Export final processed dataset
with open('./T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl', 'wb') as f:
    pickle.dump(T20_BFC_over40_df_f, f)

# Export MLM training sets (option 1 and 2)
with open('./T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl', 'wb') as f:
    pickle.dump(group_data_sickFinal_mlm1, f)

with open('./T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl', 'wb') as f:
    pickle.dump(group_data_sickFinal_mlm2, f)
```

#### 1.4 Verify Output Files

After running the notebook, you should have these files:

```
✓ DS.pkl
✓ T20.pkl
✓ BFC.pkl
✓ vocab1_new.pickle
✓ vocab2_new.pickle
✓ T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
✓ T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl
✓ T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl
```

Check file sizes to ensure they were created correctly:

```python
import os
for file in ['DS.pkl', 'T20.pkl', 'BFC.pkl']:
    size = os.path.getsize(file) / (1024 * 1024)  # MB
    print(f"{file}: {size:.2f} MB")
```

## Step 2: BERTopic Analysis

### Using the BERTopic Notebook

**File:** `1. Bertopic_over40/SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb`

#### 2.1 Launch Notebook

```bash
jupyter notebook
```

Navigate to: `1. Bertopic_over40/SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb`

#### 2.2 Configure Data Paths

Update the path to preprocessed data:

```python
# Find this cell and update the path
with open('../preprocess/T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl', 'rb') as f:
    data3 = pickle.load(f)
    T20_BFC_over40_df_f = pd.DataFrame(data3)
```

Change to:

```python
# If files are in root directory
with open('../T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl', 'rb') as f:
    data3 = pickle.load(f)
    T20_BFC_over40_df_f = pd.DataFrame(data3)
```

#### 2.3 Load Vocabulary

```python
import pickle

with open('../vocab2_new.pickle', 'rb') as f:
    vocab2 = pickle.load(f)

print(f"Vocabulary size: {len(vocab2)}")
```

#### 2.4 Create Word Dictionary

```python
## Create word dictionary
word_dict = {'PAD': 0, 'CLS': 1, 'SEP': 2, 'MASK': 3, 'UNK': 4}
for i, w in enumerate(vocab2):
    word_dict[w] = i + 4

vocab_size = len(word_dict)
print(f"Total vocabulary size: {vocab_size}")  # Should be 103
```

#### 2.5 Prepare Data

```python
# Rename columns for consistency
g_data = T20_BFC_over40_df_f
group_data_sickFinal_ndp = g_data
group_data_sickFinal_ndp.columns = ['ID', 'd2', 'AGE', 'AGE2', 'SEX', 'AGE0', 'GAIBJA']

# Reset index
sample_f_NDP = group_data_sickFinal_ndp.reset_index()
data = sample_f_NDP
print(f"Total patients: {len(data)}")
```

#### 2.6 Gender Stratification

```python
# Separate by gender
data_male = data[data['SEX'] == 1].copy()
data_female = data[data['SEX'] == 2].copy()

print(f"Male patients: {len(data_male)}")
print(f"Female patients: {len(data_female)}")
```

#### 2.7 Prepare Documents for BERTopic

```python
# Convert disease sequences to space-separated strings
def prepare_documents(df):
    documents = []
    for idx, row in df.iterrows():
        # Join disease codes with spaces (excluding 'SEP')
        doc = ' '.join([str(code) for code in row['d2'] if code != 'SEP'])
        documents.append(doc)
    return documents

docs_male = prepare_documents(data_male)
docs_female = prepare_documents(data_female)
```

#### 2.8 Train BERTopic Models

```python
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# Create custom vectorizer for disease codes
vectorizer_model = CountVectorizer(
    tokenizer=lambda x: x.split(),
    token_pattern=None,
    lowercase=False
)

# Train male model
print("Training male BERTopic model...")
topic_model_male = BERTopic(
    vectorizer_model=vectorizer_model,
    min_topic_size=50,  # Adjust based on your data
    nr_topics='auto'
)
topics_male, probs_male = topic_model_male.fit_transform(docs_male)

# Train female model
print("Training female BERTopic model...")
topic_model_female = BERTopic(
    vectorizer_model=vectorizer_model,
    min_topic_size=50,
    nr_topics='auto'
)
topics_female, probs_female = topic_model_female.fit_transform(docs_female)

print(f"Male topics discovered: {len(topic_model_male.get_topic_info())}")
print(f"Female topics discovered: {len(topic_model_female.get_topic_info())}")
```

#### 2.9 Save Models

```python
# Save male model
topic_model_male.save("my_topics_model_100pall_19y_over40_option1_male_dec20")

# Save female model
topic_model_female.save("my_topics_model_100pall_19y_over40_option1_female_dec20")

print("Models saved successfully!")
```

#### 2.10 Export Topic Information

```python
# Get topic information
topic_info_male = topic_model_male.get_topic_info()
topic_info_female = topic_model_female.get_topic_info()

# Save to Excel
topic_info_male.to_excel('topics_info_100p_over40_op1_male_dec20.xlsx', index=False)
topic_info_female.to_excel('topics_info_100p_over40_op1_female_dec20.xlsx', index=False)

print("Topic information exported to Excel!")
```

## Understanding the Results

### Topic Information Files

The Excel files contain:

| Column | Description |
|--------|-------------|
| Topic | Topic ID (-1 is outlier topic) |
| Count | Number of patients in topic |
| Name | Representative disease codes |
| Representation | Top keywords/codes for topic |

### Interpreting Topics

Example topic interpretation:

```
Topic 3: "152_220_147"
Count: 5,234 patients
Representation: ['152', '220', '147', '134', '219']
```

This indicates a multimorbidity pattern involving:
- Disease 152: [Look up in disease_codes.xlsx]
- Disease 220: [Look up in disease_codes.xlsx]
- Disease 147: [Look up in disease_codes.xlsx]

### Loading Saved Models

```python
from bertopic import BERTopic

# Load male model
topic_model_male = BERTopic.load("my_topics_model_100pall_19y_over40_option1_male_dec20")

# Get topic info
topic_info = topic_model_male.get_topic_info()
print(topic_info)

# Get specific topic details
topic_3 = topic_model_male.get_topic(3)
print(f"Topic 3 diseases: {topic_3}")
```

### Visualizing Topics

```python
# Visualize topics
fig = topic_model_male.visualize_topics()
fig.show()

# Visualize topic hierarchy
fig = topic_model_male.visualize_hierarchy()
fig.show()

# Visualize barchart for specific topic
fig = topic_model_male.visualize_barchart(top_n_topics=10)
fig.show()
```

## Troubleshooting

### Common Issues

#### 1. Memory Error

**Error:** `MemoryError: Unable to allocate array`

**Solution:**
```python
# Reduce dataset size for testing
data_sample = data.sample(n=10000, random_state=42)

# Or increase min_topic_size
topic_model = BERTopic(min_topic_size=100)  # Larger = fewer topics
```

#### 2. File Not Found

**Error:** `FileNotFoundError: [Errno 2] No such file or directory: 'DS.pkl'`

**Solution:**
```python
# Check current working directory
import os
print(os.getcwd())

# Update path accordingly
with open('/full/path/to/DS.pkl', 'rb') as f:
    data = pickle.load(f)
```

#### 3. Pickle Protocol Error

**Error:** `ValueError: unsupported pickle protocol: 5`

**Solution:**
```bash
# Install pickle5 for Python < 3.8
pip install pickle5

# Then in Python:
import pickle5 as pickle
```

#### 4. Vocabulary Size Mismatch

**Error:** Vocabulary size is not 103

**Solution:**
```python
# Rebuild vocabulary
codes_unique = [item for items in data['d2'] for item in items]
vocab2 = dict(zip(set(codes_unique), range(1, len(set(codes_unique)) + 1)))

# Save updated vocabulary
with open('vocab2_new.pickle', 'wb') as f:
    pickle.dump(vocab2, f)
```

#### 5. BERTopic Import Error

**Error:** `ModuleNotFoundError: No module named 'bertopic'`

**Solution:**
```bash
pip install bertopic
# Or with specific version
pip install bertopic==0.12.0
```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/yourusername/Multimorbidity_Bertopic/issues)
2. Review notebook cell outputs for error messages
3. Verify input data formats match expected schemas
4. Check Python and package versions

## Advanced Usage

### Customizing BERTopic Parameters

```python
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
from hdbscan import HDBSCAN

# Custom UMAP settings
umap_model = UMAP(
    n_neighbors=15,
    n_components=5,
    min_dist=0.0,
    metric='cosine',
    random_state=42
)

# Custom HDBSCAN settings
hdbscan_model = HDBSCAN(
    min_cluster_size=50,
    metric='euclidean',
    cluster_selection_method='eom',
    prediction_data=True
)

# Create BERTopic with custom models
topic_model = BERTopic(
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer_model,
    min_topic_size=50
)
```

### Analyzing Specific Disease of Interest (DOI)

```python
# Example: Find patients with Stomach cancer (code 102)
def has_disease(row, disease_code):
    return str(disease_code) in row['d2']

data['has_stomach_cancer'] = data.apply(lambda x: has_disease(x, 102), axis=1)

# Stratify analysis
data_with_sc = data[data['has_stomach_cancer'] == True]
data_without_sc = data[data['has_stomach_cancer'] == False]

print(f"Patients with stomach cancer: {len(data_with_sc)}")
print(f"Patients without stomach cancer: {len(data_without_sc)}")
```

### Age Group Analysis

```python
# Create age groups
bins = [0, 20, 40, 65, 110]
labels = ['below 20', '20-40', '40-65', 'over 65']
data['AgeGroup'] = pd.cut(data['AGE0'], bins=bins, labels=labels, right=False)

# Analyze by age group
for age_group in ['40-65', 'over 65']:
    data_age = data[data['AgeGroup'] == age_group]
    print(f"\n{age_group}: {len(data_age)} patients")

    # Run BERTopic for this age group
    docs_age = prepare_documents(data_age)
    topic_model_age = BERTopic(vectorizer_model=vectorizer_model)
    topics_age, _ = topic_model_age.fit_transform(docs_age)
```

### Statistical Analysis

```python
from scipy.stats import chi2_contingency

# Chi-square test for gender and age distribution
contingency_table = pd.crosstab(data['SEX'], data['AgeGroup'])
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p_value}")
```

### Exporting for Publication

```python
# Summary statistics for paper
summary_stats = {
    'Total Patients': len(data),
    'Male': len(data[data['SEX'] == 1]),
    'Female': len(data[data['SEX'] == 2]),
    'Age 40-64': len(data[data['AgeGroup'] == '40-65']),
    'Age 65+': len(data[data['AgeGroup'] == 'over 65']),
    'Topics (Male)': len(topic_model_male.get_topic_info()),
    'Topics (Female)': len(topic_model_female.get_topic_info())
}

# Save to CSV
pd.DataFrame([summary_stats]).T.to_csv('summary_statistics.csv', header=['Value'])
```

## Next Steps

After completing the analysis:

1. **Interpret Topics**: Map disease codes to clinical meanings
2. **Validate Results**: Compare with clinical literature
3. **Statistical Testing**: Perform chi-square, t-tests for gender/age differences
4. **Visualize Findings**: Create publication-quality figures
5. **Write Paper**: Use results for journal manuscript

## Citation

When using this code, please cite:

```bibtex
@article{multimorbidity_bertopic_2024,
  title={Multimorbidity Pattern Discovery using BERTopic in Patients Aged 40 and Above},
  author={[Your Name]},
  journal={[Journal Name]},
  year={2024}
}
```

## Support

For additional help:
- **Email**: [your.email@institution.edu]
- **GitHub Issues**: [Repository Issues Page]
- **Documentation**: See README.md and DIRECTORY_STRUCTURE.md
