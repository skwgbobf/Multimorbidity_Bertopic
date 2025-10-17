# Multimorbidity Analysis using BERTopic

## Overview

This repository contains the implementation and analysis code for studying multimorbidity patterns in patients aged 40 and above using BEHRT (BERT for Electronic Health Records) preprocessing and BERTopic modeling. The study analyzes disease trajectories and comorbidity patterns using longitudinal health records spanning from 2002 to 2021.

## Project Description

This research focuses on:
- **Population**: Patients aged 40 and above from a healthcare database
- **Time Period**: 2002-2021 (19 years)
- **Methods**: BEHRT data preprocessing and BERTopic topic modeling
- **Analysis**: Gender-stratified multimorbidity pattern discovery
- **Total Patients**: 331,811 patients over age 40
- **Sample Distribution**:
  - Male: 154,121 patients (46.4%)
  - Female: 177,690 patients (53.6%)

## Key Features

1. **Data Preprocessing Pipeline** (BEHRT format)
   - Temporal sequence creation with disease codes
   - Age tracking over time
   - Gender and regional information integration
   - Train/test data splitting (50/50 for MLM tasks)

2. **Disease Code Analysis**
   - Disease code vocabulary creation (103 disease codes)
   - ICD-based disease categorization
   - Temporal disease sequence tracking

3. **BERTopic Modeling**
   - Gender-stratified topic modeling (male/female)
   - Multimorbidity pattern discovery
   - Topic information extraction and analysis

4. **Data Products**
   - Preprocessed datasets in pickle format
   - Trained BERTopic models
   - Topic analysis results in Excel format

## Repository Structure

```
GIT/
├── README.md                           # This file
├── DIRECTORY_STRUCTURE.md              # Detailed directory documentation
├── USAGE_GUIDE.md                      # Step-by-step usage instructions
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Git ignore rules
│
├── Data Files (Root Level)
│   ├── disease_codes.xlsx              # Disease code definitions (13.5 KB)
│   ├── DS.pkl                          # Disease codes pickle (5.8 KB)
│   ├── BFC.pkl                         # Basic patient info (21.6 MB)
│   ├── T20.pkl                         # Main disease records (119.6 MB)
│   ├── T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl    # BERTopic input (109.2 MB)
│   ├── T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl  # MLM option 1 (54.1 MB)
│   └── T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl  # MLM option 2 (54.1 MB)
│
├── Notebooks
│   ├── S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb
│   │   └── Main preprocessing notebook for BEHRT data (over 40 patients)
│   ├── SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb
│   │   └── Simplified preprocessing workflow
│   └── SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb
│       └── Preprocessing for all ages (reference)
│
└── 1. Bertopic_over40/
    ├── SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb
    │   └── BERTopic analysis with gender stratification
    ├── my_topics_model_100pall_19y_over40_option1_male_dec20      # Male BERTopic model (722 MB)
    ├── my_topics_model_100pall_19y_over40_option1_female_dec20    # Female BERTopic model (725 MB)
    ├── topics_info_100p_over40_op1_male_dec20.xlsx                # Male topic results
    ├── topics_info_100p_over40_op1_male_dec20_2.xlsx              # Male topic results (alt)
    └── topics_info_100p_over40_op1_female_dec20.xlsx              # Female topic results
```

## Data Files Description

### Input Data
- **disease_codes.xlsx**: Disease code definitions and washout periods
- **DS.pkl**: Disease codes dataset (columns: d, dname, wash_out)
- **BFC.pkl**: Basic patient information (ID, SEX, AGE, GAIBJA)
- **T20.pkl**: Raw disease records (YEAR, ID, d)

### Processed Data
- **T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl**:
  - Complete dataset for BERTopic analysis (100% of over-40 patients)
  - Contains disease sequences, age sequences, demographics

- **T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl**:
  - Masked Language Model training data (Option 1: 50% split)
  - Patients with ID ending in 0, 2, 4, 6, 8

- **T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl**:
  - Masked Language Model training data (Option 2: 50% split)
  - Patients with ID ending in 1, 3, 5, 7, 9

### Output Data
- **BERTopic Models**: Trained models for male and female populations
- **Topic Information**: Excel files containing discovered multimorbidity patterns

## Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook/Lab
- Required Python packages (see requirements.txt)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/Multimorbidity_Bertopic.git
cd Multimorbidity_Bertopic

# Install dependencies
pip install -r requirements.txt

# Optional: Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Quick Start

1. **Data Preprocessing** (BEHRT format):
   ```bash
   jupyter notebook "SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb"
   ```
   This notebook:
   - Loads raw CSV files (DS.csv, T20.csv, BFC.csv)
   - Filters patients aged 40+
   - Creates temporal sequences
   - Exports preprocessed pickle files

2. **BERTopic Analysis**:
   ```bash
   jupyter notebook "1. Bertopic_over40/SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb"
   ```
   This notebook:
   - Loads preprocessed data
   - Performs gender-stratified BERTopic modeling
   - Generates topic analysis results
   - Exports models and Excel reports

### Detailed Workflow

See [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed step-by-step instructions.

## Data Schema

### Disease Sequence Format
```python
{
    'ID': patient_id,
    'd2': ['219', 'SEP', '147', 'SEP', ...],      # Disease codes with separators
    'AGE2': ['55', '55', '56', '56', ...],        # Age at each disease occurrence
    'SEX': 1 or 2,                                 # 1=Male, 2=Female
    'AGE_y': baseline_age,                         # Age at baseline
    'GAIBJA': region_code                          # Regional code
}
```

### Disease Code Examples
- 101: Esophageal cancer
- 102: Stomach cancer
- 103: Liver cancer
- 138: Atrial fibrillation and flutter
- 147, 152, 162: Various chronic conditions
- 219, 220, 221: Chronic disease codes

## Methodology

### BEHRT Data Preprocessing
1. **Data Integration**: Merge disease records (T20) with patient demographics (BFC)
2. **Age Filtering**: Select patients aged 40 and above
3. **Sequence Creation**:
   - Group diseases by patient and year
   - Create temporal sequences with 'SEP' separators
   - Track age at each disease occurrence
4. **Data Splitting**: 50/50 split for MLM training based on patient ID

### BERTopic Analysis
1. **Data Preparation**: Convert disease sequences to document format
2. **Gender Stratification**: Separate analysis for male and female populations
3. **Topic Modeling**: Apply BERTopic to discover multimorbidity patterns
4. **Result Export**: Save models and topic information

## Results

### Patient Demographics (Over 40)
- **Total Patients**: 331,811
- **Age Groups**:
  - 40-64 years: 239,561 patients (72.2%)
  - 65+ years: 92,250 patients (27.8%)
- **Gender Distribution**:
  - Male 40-64: 116,079 patients
  - Male 65+: 38,042 patients
  - Female 40-64: 123,482 patients
  - Female 65+: 54,208 patients

### Output Files
- Gender-specific BERTopic models (male/female)
- Topic information spreadsheets with multimorbidity patterns
- Statistical analysis of age and gender distributions

## Citation

If you use this code or data in your research, please cite:

```bibtex
@article{multimorbidity_bertopic_2024,
  title={Multimorbidity Pattern Discovery using BERTopic in Patients Aged 40 and Above},
  author={[Your Name]},
  journal={[Journal Name]},
  year={2024}
}
```

## License

[Specify your license here - e.g., MIT, Apache 2.0, etc.]

## Contact

For questions or collaborations, please contact:
- Email: [your.email@institution.edu]
- Institution: [Your Institution]

## Acknowledgments

- BEHRT framework for EHR data preprocessing
- BERTopic library for topic modeling
- [Any funding sources or collaborators]

## Version History

- **v1.0.0** (2024): Initial release
  - BEHRT preprocessing pipeline for over-40 patients
  - Gender-stratified BERTopic analysis
  - 19-year longitudinal data (2002-2021)

## Known Issues and Limitations

1. **Data Privacy**: All patient IDs are anonymized. Ensure compliance with data privacy regulations.
2. **Large Files**: Model files are large (>700MB each). Git LFS is recommended.
3. **Computational Requirements**: BERTopic modeling requires significant RAM (16GB+ recommended).
4. **Washout Periods**: Disease-specific washout periods (5 years for cancers) are applied.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Future Work

- Extension to younger age groups
- Time-series prediction models
- Integration with clinical outcomes
- External validation on different datasets
