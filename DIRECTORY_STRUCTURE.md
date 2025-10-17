# Directory Structure

This document provides a detailed breakdown of the repository structure and file descriptions.

## Repository Layout

```
Multimorbidity_Bertopic/
│
├── README.md                       # Main documentation
├── DIRECTORY_STRUCTURE.md          # This file
├── USAGE_GUIDE.md                  # Step-by-step usage instructions
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore patterns
│
├── Data Files (Root Level)
│   ├── disease_codes.xlsx          # Disease code reference
│   ├── DS.pkl                      # Disease codes (pickle)
│   ├── BFC.pkl                     # Patient demographics
│   ├── T20.pkl                     # Raw disease records
│   ├── T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
│   ├── T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl
│   └── T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl
│
├── Preprocessing Notebooks
│   ├── S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb
│   ├── SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb
│   └── SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb
│
└── 1. Bertopic_over40/
    ├── SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb
    ├── my_topics_model_100pall_19y_over40_option1_male_dec20/
    ├── my_topics_model_100pall_19y_over40_option1_female_dec20/
    ├── topics_info_100p_over40_op1_male_dec20.xlsx
    ├── topics_info_100p_over40_op1_male_dec20_2.xlsx
    └── topics_info_100p_over40_op1_female_dec20.xlsx
```

## File Descriptions

### Root Directory Files

#### Documentation Files
- **README.md** (This will be created)
  - Main project documentation
  - Overview, installation, usage instructions
  - Citation information

- **DIRECTORY_STRUCTURE.md** (This file)
  - Detailed file and folder descriptions
  - Data schema documentation

- **USAGE_GUIDE.md** (This will be created)
  - Step-by-step usage instructions
  - Code examples
  - Troubleshooting guide

- **requirements.txt** (This will be created)
  - Python package dependencies
  - Version specifications

- **.gitignore** (This will be created)
  - Git ignore patterns
  - Excludes large data files, temporary files

### Data Files (Root Level)

#### Input Data Files

**disease_codes.xlsx** (13.5 KB)
- **Description**: Disease code definitions and metadata
- **Format**: Excel spreadsheet
- **Columns**:
  - `d`: Disease code (integer)
  - `dname`: Disease name (string)
  - `wash_out`: Washout period in years (integer)
- **Sample Data**:
  ```
  d=101, dname="Esophageal cancer", wash_out=5
  d=102, dname="Stomach cancer", wash_out=5
  d=103, dname="Liver cancer", wash_out=5
  ```
- **Usage**: Reference for disease code interpretation

**DS.pkl** (5.8 KB)
- **Description**: Pickled version of disease codes
- **Format**: Pandas DataFrame (pickle)
- **Structure**: Same as disease_codes.xlsx
- **Rows**: 103 disease codes
- **Usage**: Fast loading of disease code mappings

**BFC.pkl** (21.6 MB)
- **Description**: Basic patient demographic information
- **Format**: Pandas DataFrame (pickle)
- **Columns**:
  - `ID`: Patient identifier (integer)
  - `SEX`: Gender (1=Male, 2=Female)
  - `AGE`: Age at baseline (integer)
  - `GAIBJA`: Regional code (integer 1-7)
- **Rows**: 673,818 total patients
- **Sample**:
  ```python
  ID=1, SEX=2, AGE=51, GAIBJA=2
  ID=2, SEX=2, AGE=19, GAIBJA=6
  ID=3, SEX=2, AGE=71, GAIBJA=7
  ```
- **Gender Distribution**:
  - Male (SEX=1): 323,597 (48.0%)
  - Female (SEX=2): 350,221 (52.0%)

**T20.pkl** (119.6 MB)
- **Description**: Raw disease occurrence records
- **Format**: Pandas DataFrame (pickle)
- **Columns**:
  - `YEAR`: Year of disease occurrence (2002-2021)
  - `ID`: Patient identifier
  - `d`: Disease code
- **Rows**: 4,984,056 disease records
- **Time Range**: 2002-2021 (19 years)
- **Sample**:
  ```python
  YEAR=2006, ID=1, d=219
  YEAR=2007, ID=1, d=219
  YEAR=2009, ID=1, d=221
  ```

#### Processed Data Files

**T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl** (109.2 MB)
- **Description**: Complete preprocessed dataset for BERTopic analysis
- **Population**: Patients aged 40+ at baseline
- **Format**: Pandas DataFrame (pickle)
- **Rows**: 331,811 patients
- **Columns**:
  - `ID`: Patient identifier
  - `d2`: Disease sequence (list) with 'SEP' separators
  - `AGE_x`: Age sequence (list)
  - `AGE2`: Age sequence without trailing separator
  - `SEX`: Gender (1=Male, 2=Female)
  - `AGE_y`: Baseline age
  - `GAIBJA`: Regional code
- **Data Structure Example**:
  ```python
  {
      'ID': 1,
      'd2': ['219', 'SEP', '219', 'SEP', '221', 'SEP', ...],
      'AGE2': ['55', '55', '56', '56', '58', '58', ...],
      'SEX': 2,
      'AGE_y': 51,
      'GAIBJA': 2
  }
  ```
- **Usage**: Input for BERTopic gender-stratified analysis

**T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl** (54.1 MB)
- **Description**: MLM training data (Option 1)
- **Population**: 50% of over-40 patients
- **Selection Criteria**: Patient IDs ending in 0, 2, 4, 6, 8
- **Rows**: 165,986 patients
- **Format**: Same structure as BERTopic file
- **Additional Columns**:
  - `index`: Original index
  - `fold2`: Data split indicator (0 for this option)
- **Usage**: Masked Language Model training

**T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl** (54.1 MB)
- **Description**: MLM training data (Option 2)
- **Population**: Complementary 50% of over-40 patients
- **Selection Criteria**: Patient IDs ending in 1, 3, 5, 7, 9
- **Rows**: 165,825 patients
- **Format**: Same structure as MLM Option 1
- **Additional Columns**:
  - `index`: Original index
  - `fold2`: Data split indicator (1 for this option)
- **Usage**: Complementary MLM training set or validation

### Preprocessing Notebooks

**S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb** (1.4 MB)
- **Description**: Main comprehensive preprocessing notebook
- **Purpose**: Full BEHRT data preprocessing pipeline for over-40 patients
- **Key Steps**:
  1. Import raw CSV files (DS.csv, T20.csv, BFC.csv)
  2. Convert CSV to pickle format
  3. Filter patients aged 40+
  4. Create age-adjusted temporal sequences (AGE2 = YEAR - 2002 + AGE)
  5. Merge disease records with demographics
  6. Create vocabulary (vocab1, vocab2)
  7. Group diseases by patient and year
  8. Add 'SEP' separators between years
  9. Split data for MLM (options 1 and 2)
  10. Export processed datasets
- **Output Files**:
  - DS.pkl
  - T20.pkl
  - BFC.pkl
  - vocab1_new.pickle
  - vocab2_new.pickle
  - T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
  - T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl
  - T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl
- **Sections**:
  - Part I: Original Data Import
  - Part II: Vocabulary and Path
  - Part III: MLM Data Preprocessing

**SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb** (118.9 KB)
- **Description**: Simplified/streamlined preprocessing notebook
- **Purpose**: Faster preprocessing workflow with fewer intermediate steps
- **Key Differences from S1F**:
  - Fewer exploratory visualizations
  - Streamlined data grouping
  - Focuses on essential preprocessing steps
- **Recommended for**: Production runs after initial exploration

**SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb** (1.4 MB)
- **Description**: Preprocessing notebook for all ages (reference)
- **Purpose**: Compare preprocessing for all ages vs. over-40
- **Key Difference**: No age filtering (includes all 673,818 patients)
- **Usage**: Reference for methodology, not used in primary analysis

### BERTopic Analysis Folder: `1. Bertopic_over40/`

**SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb** (18.0 MB)
- **Description**: Complete BERTopic analysis with gender stratification
- **Purpose**: Discover multimorbidity patterns separately for males and females
- **Input Data**: T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
- **Key Steps**:
  1. Load preprocessed data (331,811 patients over 40)
  2. Load vocabulary (vocab2_new.pkl)
  3. Create word dictionary (103 disease codes)
  4. Prepare document format for BERTopic
  5. Stratify by gender:
     - Male: 154,121 patients
     - Female: 177,690 patients
  6. Age group analysis (40-64 vs. 65+)
  7. Run BERTopic separately for each gender
  8. Export models and topic information
  9. Statistical analysis (chi-square tests, gender/age distributions)
- **Output Files**:
  - Male BERTopic model
  - Female BERTopic model
  - Topic information Excel files
  - Age/gender distribution statistics

**my_topics_model_100pall_19y_over40_option1_male_dec20/** (722.4 MB)
- **Description**: Trained BERTopic model for male patients
- **Population**: Male patients aged 40+ (154,121 patients)
- **Format**: BERTopic model directory (binary files)
- **Contents**:
  - Model parameters
  - Embeddings
  - Topic representations
  - Document-topic distributions
- **Training Data**: Male subset of T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
- **Usage**: Load with BERTopic.load() for inference or analysis

**my_topics_model_100pall_19y_over40_option1_female_dec20/** (725.3 MB)
- **Description**: Trained BERTopic model for female patients
- **Population**: Female patients aged 40+ (177,690 patients)
- **Format**: BERTopic model directory (binary files)
- **Contents**: Same structure as male model
- **Training Data**: Female subset of T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
- **Usage**: Load with BERTopic.load() for inference or analysis

**topics_info_100p_over40_op1_male_dec20.xlsx** (8.3 KB)
- **Description**: Topic analysis results for male patients
- **Format**: Excel spreadsheet
- **Contents**:
  - Topic IDs
  - Representative diseases per topic
  - Topic prevalence
  - Top keywords/disease codes per topic
- **Usage**: Interpret multimorbidity patterns in male population

**topics_info_100p_over40_op1_male_dec20_2.xlsx** (8.3 KB)
- **Description**: Alternative or updated topic analysis for males
- **Format**: Excel spreadsheet
- **Purpose**: May contain refined topics or different parameterization
- **Usage**: Compare with primary male topic results

**topics_info_100p_over40_op1_female_dec20.xlsx** (8.1 KB)
- **Description**: Topic analysis results for female patients
- **Format**: Excel spreadsheet
- **Contents**: Same structure as male topic file
- **Usage**: Interpret multimorbidity patterns in female population

## Data Flow Diagram

```
Raw CSV Files (External)
    ├── DS.csv (disease codes)
    ├── T20.csv (disease records)
    └── BFC.csv (patient demographics)
           ↓
    [S1F/SFI Preprocessing Notebook]
           ↓
Pickle Files (Root)
    ├── DS.pkl
    ├── BFC.pkl
    ├── T20.pkl
    ├── vocab1_new.pickle
    └── vocab2_new.pickle
           ↓
    [Merge, Filter Age 40+, Create Sequences]
           ↓
Processed Datasets (Root)
    ├── T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl
    ├── T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl
    └── T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl
           ↓
    [SIIF BERTopic Notebook]
           ↓
    [Gender Stratification]
    ├── Male Subset (154,121)
    └── Female Subset (177,690)
           ↓
    [BERTopic Modeling]
           ↓
Output Files (1. Bertopic_over40/)
    ├── my_topics_model_*_male_dec20/
    ├── my_topics_model_*_female_dec20/
    ├── topics_info_*_male_dec20.xlsx
    └── topics_info_*_female_dec20.xlsx
```

## Data Schema Details

### Disease Sequence Structure

```python
# Example patient record
{
    'ID': 1,
    'd2': [
        '219',      # Disease code
        'SEP',      # Year separator
        '219',      # Same disease, different year
        'SEP',
        '221',      # Different disease
        'SEP',
        # ... continues
    ],
    'AGE_x': [55, 55, 56, 56, 58, 58, ...],  # Age at each event
    'AGE2': [55, 55, 56, 56, 58, 58, ...],   # Age without trailing separator
    'SEX': 2,       # Female
    'AGE_y': 51,    # Baseline age (year 2002)
    'GAIBJA': 2     # Region code
}
```

### Age Calculation
```
AGE2 = (YEAR - 2002) + AGE_baseline

Example:
- Patient baseline age in 2002: 51
- Disease occurrence in 2006: AGE2 = (2006 - 2002) + 51 = 55
- Disease occurrence in 2010: AGE2 = (2010 - 2002) + 51 = 59
```

### Vocabulary Structure

```python
# Word dictionary (103 total items)
word_dict = {
    'PAD': 0,       # Padding token
    'CLS': 1,       # Classification token
    'SEP': 2,       # Separator token
    'MASK': 3,      # Mask token for MLM
    'UNK': 4,       # Unknown token
    '101': 5,       # Disease code 101 (Esophageal cancer)
    '102': 6,       # Disease code 102 (Stomach cancer)
    # ... 98 more disease codes ...
}
```

## File Size Summary

| File Type | Count | Total Size |
|-----------|-------|------------|
| Pickle Data Files | 7 | ~334 MB |
| BERTopic Models | 2 | ~1.45 GB |
| Jupyter Notebooks | 4 | ~20.8 MB |
| Excel Files | 3 | ~24 KB |
| **Total** | **16** | **~1.8 GB** |

## Key Statistics

### Patient Demographics (Over 40)
- **Total Patients**: 331,811
- **Male**: 154,121 (46.4%)
- **Female**: 177,690 (53.6%)

### Age Distribution (Over 40)
- **40-64 years**: 239,561 (72.2%)
  - Male: 116,079
  - Female: 123,482
- **65+ years**: 92,250 (27.8%)
  - Male: 38,042
  - Female: 54,208

### Disease Records
- **Total Records**: 3,821,172 (for over-40 patients)
- **Time Span**: 2002-2021 (19 years)
- **Unique Disease Codes**: 103

### Data Splits (MLM)
- **Option 1**: 165,986 patients (IDs ending in 0,2,4,6,8)
- **Option 2**: 165,825 patients (IDs ending in 1,3,5,7,9)

## Notes

1. **Large Files**: BERTopic models are >700MB each. Use Git LFS for version control.
2. **Privacy**: All patient IDs are anonymized. Ensure compliance with IRB and data privacy regulations.
3. **Reproducibility**: Random seeds should be set in BERTopic notebook for reproducible results.
4. **Memory Requirements**: Loading full datasets requires 16GB+ RAM.
5. **Processing Time**:
   - Preprocessing: ~10-30 minutes
   - BERTopic training: ~1-3 hours per gender (depends on hardware)
