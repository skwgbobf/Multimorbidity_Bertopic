# Multimorbidity Analysis using BERTopic

## Overview

This repository contains the implementation and analysis code for studying multimorbidity patterns in patients aged 40 and above using BEHRT (BERT for Electronic Health Records) preprocessing and BERTopic modeling. The study analyzes disease trajectories and comorbidity patterns using longitudinal health records spanning from 2002 to 2021.

## Project Description

This research focuses on:
- **Population**: Patients aged 40 and above from a healthcare database
- **Time Period**: 2002-2021 (19 years)
- **Methods**: BEHRT data preprocessing and BERTopic topic modeling
- **Analysis**: Gender-stratified multimorbidity pattern discovery
- **Manuscript Cohort**: 168,529 patients over age 40 with ≥6 years healthcare history
- **Sample Distribution**:
  - Male: 73,157 patients (43.4%)
  - Female: 95,372 patients (56.6%)
- **Topics Discovered**:
  - Female: 19 distinct multimorbidity patterns
  - Male: 20 distinct multimorbidity patterns

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
   - Topic information extraction with c-TF-IDF weights
   - 19 female topics + 20 male topics (manuscript-final)

4. **Model Evaluation**
   - Coherence metrics (C_v, C_uci, C_npmi)
   - Diversity metrics (unique words ratio, Jaccard distance)
   - Quality validation: C_v ~0.50 (GOOD), Jaccard ~0.76-0.78

5. **Data Products**
   - Preprocessed datasets in pickle format
   - Topic analysis results in CTFIDF Excel format
   - Patient demographics (non-PHI)
   - Evaluation metrics and reports

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
├── scripts/
│   └── evaluate_from_excel.py          # Topic evaluation (coherence & diversity metrics)
│
├── results/
│   └── evaluation/
│       ├── EVALUATION_RESULTS_SUMMARY.md        # Complete evaluation report
│       ├── coherence_female.csv                 # Female model metrics
│       ├── coherence_male.csv                   # Male model metrics
│       └── model_evaluation_summary.csv         # Combined results
│
└── 1. Bertopic_over40/
    └── Shared_BERtopic_over40/         # ✅ MANUSCRIPT-FINAL ANALYSIS
        ├── Final_SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_feb21_shared_afterre_july29F_Aug23.ipynb
        │   └── BERTopic analysis with gender stratification (manuscript version)
        ├── 100pall_19y_over40_option1_female_dec20_CTFIDF_aug23.xlsx  # Female: 19 topics
        ├── 100pall_19y_over40_option1_male_dec20_CTFIDF_aug23.xlsx    # Male: 20 topics
        └── Bertopic_over40_patientsID_aug23.xlsx                      # 168,529 patients
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

### Output Data (Manuscript-Final)
- **Topic Results (CTFIDF Format)**:
  - `100pall_19y_over40_option1_female_dec20_CTFIDF_aug23.xlsx`: 19 topics × 10 words with c-TF-IDF weights
  - `100pall_19y_over40_option1_male_dec20_CTFIDF_aug23.xlsx`: 20 topics × 10 words with c-TF-IDF weights
- **Patient Demographics**: `Bertopic_over40_patientsID_aug23.xlsx` (168,529 patients, non-PHI)
- **Evaluation Metrics**: Coherence and diversity scores in `results/evaluation/`

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

2. **BERTopic Analysis** (Manuscript Version):
   ```bash
   jupyter notebook "1. Bertopic_over40/Shared_BERtopic_over40/Final_SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_feb21_shared_afterre_july29F_Aug23.ipynb"
   ```
   This notebook:
   - Loads preprocessed data (168,529 patients)
   - Performs gender-stratified BERTopic modeling
   - Generates 19 female + 20 male topics
   - Exports CTFIDF results with c-TF-IDF weights

3. **Model Evaluation**:
   ```bash
   python scripts/evaluate_from_excel.py
   ```
   This script:
   - Loads CTFIDF topic results
   - Calculates coherence metrics (C_v, C_uci, C_npmi)
   - Calculates diversity metrics
   - Exports evaluation reports to `results/evaluation/`

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

### Manuscript Cohort (168,529 Patients, ≥6 years healthcare history)
- **Total Patients**: 168,529
- **Gender Distribution**:
  - Male: 73,157 patients (43.4%)
  - Female: 95,372 patients (56.6%)
- **Age Range**: 40-90 years
  - Mean age at baseline: 55.9 years (SD: 9.9)
  - Mean age at analysis: 58.5 years (SD: 9.7)

### Topic Discovery Results
**Female Model (19 Topics):**
- C_v coherence: 0.500 (GOOD quality)
- Jaccard distance: 0.756 (well-separated topics)
- Topic format: CTFIDF with c-TF-IDF weights

**Male Model (20 Topics):**
- C_v coherence: 0.503 (GOOD quality)
- Jaccard distance: 0.780 (well-separated topics)
- Topic format: CTFIDF with c-TF-IDF weights

### Output Files (Manuscript-Final)
- Gender-specific topic results in CTFIDF format (Excel)
- Patient demographics (non-PHI, Excel)
- Evaluation metrics and comprehensive reports (CSV + Markdown)
- See `results/evaluation/EVALUATION_RESULTS_SUMMARY.md` for details

## Data and Code Availability

All analysis code, topic results, and evaluation metrics are publicly available in this repository:

**Key Files:**
- Analysis Notebook: `1. Bertopic_over40/Shared_BERtopic_over40/Final_SIIF...Aug23.ipynb`
- Female Topics: `1. Bertopic_over40/Shared_BERtopic_over40/100pall_19y_over40_option1_female_dec20_CTFIDF_aug23.xlsx` (19 topics)
- Male Topics: `1. Bertopic_over40/Shared_BERtopic_over40/100pall_19y_over40_option1_male_dec20_CTFIDF_aug23.xlsx` (20 topics)
- Patient Demographics: `1. Bertopic_over40/Shared_BERtopic_over40/Bertopic_over40_patientsID_aug23.xlsx` (168,529 patients, non-PHI)
- Evaluation Results: `results/evaluation/` (coherence and diversity metrics)

**Note:** Individual patient-level health records cannot be shared due to privacy regulations.

## Citation

If you use this code or analysis in your research, please cite:

```bibtex
@article{multimorbidity_bertopic_2025,
  title={Multimorbidity Pattern Discovery using BERTopic in Patients Aged 40 and Above},
  author={[Your Name]},
  journal={[Journal Name]},
  year={2025},
  note={Code and analysis available at: https://github.com/skwgbobf/Multimorbidity_Bertopic}
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

- **v1.0.0** (2025-10-18): Manuscript-final release
  - BEHRT preprocessing pipeline for over-40 patients
  - Gender-stratified BERTopic analysis (19 female + 20 male topics)
  - 19-year longitudinal data (2002-2021)
  - CTFIDF format topic results with c-TF-IDF weights
  - Comprehensive evaluation metrics (coherence & diversity)
  - 168,529 patients with ≥6 years healthcare history

## Known Issues and Limitations

1. **Data Privacy**: All patient IDs are anonymized. Individual patient health records cannot be shared due to privacy regulations.
2. **Trained Models Not Included**: BERTopic model files are excluded from repository due to size (>700MB each). Topic results (CTFIDF format) and evaluation metrics are provided instead.
3. **Computational Requirements**: BERTopic modeling requires significant RAM (16GB+ recommended).
4. **Washout Periods**: Disease-specific washout periods (5 years for cancers) are applied.
5. **Cohort Selection**: Final manuscript cohort (168,529 patients) represents patients with ≥6 years of healthcare history, a subset of the full 331,811 over-40 population.

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Future Work

- Extension to younger age groups
- Time-series prediction models
- Integration with clinical outcomes
- External validation on different datasets
