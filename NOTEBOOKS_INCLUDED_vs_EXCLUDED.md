# Notebook Files: What's Included vs Excluded from GitHub

**Date:** 2025-10-18
**Repository:** https://github.com/skwgbobf/Multimorbidity_Bertopic

---

## ✅ INCLUDED Notebooks (Will Upload to GitHub)

### 1. Primary BERTopic Analysis (MANUSCRIPT FINAL VERSION)
**File:** `1. Bertopic_over40/Shared_BERtopic_over40/Final_SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_feb21_shared_afterre_july29F_Aug23.ipynb`
- **Size:** 16MB
- **Purpose:** FINAL manuscript analysis with gender stratification
- **Status:** ✅ INCLUDE - This is the MANUSCRIPT-READY analysis
- **Contains:** Complete BERTopic pipeline producing 19 female + 20 male topics for 168,529 patients
- **Key Features:**
  - Analysis Date: August 2023 (final version)
  - Output Format: CTFIDF (Word, c-TF-IDF, Topic)
  - Patients: 168,529 (95,372 female, 73,157 male)
  - Topics: 19 female, 20 male

### 2. Updated Preprocessing Notebook (October 2025)
**File:** `SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb`
- **Purpose:** Current/updated BEHRT preprocessing workflow
- **Status:** ✅ INCLUDE - This is the CURRENT version to use
- **Contains:** Simplified preprocessing steps for over-40 patients

---

## ❌ EXCLUDED Notebooks (Will NOT Upload to GitHub)

### 1. Parent Directory BERTopic Notebook (Superseded)
**File:** `1. Bertopic_over40/SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_dec20_jan29.ipynb`
- **Size:** 18MB
- **Status:** ❌ EXCLUDE - Superseded by Shared/Aug23 final version
- **Reason:** Earlier analysis version; manuscript uses refined Shared directory version
- **Differences from manuscript:**
  - Different patient cohort (likely full 331K vs. refined 168K)
  - Different topic counts (20/21 vs. 19/20)
  - Different output format (topics_info vs. CTFIDF)

### 2. Old Preprocessing Notebook (Jan 2029 version)
**File:** `SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb`
- **Size:** 117KB
- **Status:** ❌ EXCLUDE - Superseded by oct2025 version
- **Reason:** Older version, replaced by the October 2025 update

### 2. Detailed Preprocessing Notebook
**File:** `S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb`
- **Size:** 1.4MB
- **Status:** ❌ EXCLUDE - Too detailed/sensitive
- **Reason:** Contains intermediate preprocessing steps with potentially sensitive code

### 3. Detailed Preprocessing Notebook
**File:** `S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb`
- **Size:** 1.4MB
- **Status:** ❌ EXCLUDE - Too detailed/sensitive
- **Reason:** Contains intermediate preprocessing steps with potentially sensitive code

### 4. All-Ages Preprocessing Notebook
**File:** `SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb`
- **Size:** 1.4MB
- **Status:** ❌ EXCLUDE - Not used in manuscript
- **Reason:** Processes all ages, not just over-40 (not relevant to published analysis)

### 5. Draft Analyses (new/ subdirectory)
**Directory:** `1. Bertopic_over40/new/`
- **Status:** ❌ EXCLUDE - Contains draft versions
- **Reason:** Alternative analyses and older draft versions not used in final manuscript

---

## 📋 Summary Table

| Notebook | Status | Reason |
|----------|--------|--------|
| `SIIF.MLM_BertTopic...jan29.ipynb` | ✅ **INCLUDE** | Primary BERTopic analysis |
| `SFI...oct2025.ipynb` | ✅ **INCLUDE** | Current preprocessing workflow |
| `SFI...Jan29.ipynb` | ❌ **EXCLUDE** | Outdated (replaced by oct2025) |
| `S1F...jan29.ipynb` | ❌ **EXCLUDE** | Too detailed/sensitive |
| `SI...jan29.ipynb` | ❌ **EXCLUDE** | All-ages (not used) |

---

## 🔍 How .gitignore Works

The [.gitignore](file:///C:/Data/Thesis_F/Multimorbidity_Support/GIT/.gitignore) file has been configured to:

### Exclude these specific files:
```gitignore
# Lines 286-288 in .gitignore:
S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb
SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb
SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb
```

### Force include the October 2025 version:
```gitignore
# Line ~311 in .gitignore:
!SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb
```

---

## ✅ Verification Checklist

Before pushing to GitHub, verify:

```bash
cd "C:\Data\Thesis_F\Multimorbidity_Support\GIT"

# These should be IGNORED (excluded):
git check-ignore S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb
git check-ignore SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb
git check-ignore SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb
# Each should output the filename if correctly ignored

# This should be TRACKED (included):
git check-ignore SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb
# Should output NOTHING (file is tracked, not ignored)

# Verify git status
git status
# The oct2025 notebook should appear as tracked
# The other three should NOT appear at all
```

---

## 📝 For Manuscript Documentation

When referencing preprocessing in your manuscript:

**Correct reference:**
> "Data preprocessing was performed using BEHRT format as documented in
> SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb,
> available at https://github.com/skwgbobf/Multimorbidity_Bertopic"

**Or more generally:**
> "Complete preprocessing and analysis code is available at
> https://github.com/skwgbobf/Multimorbidity_Bertopic"

---

## 🔒 Why These Exclusions?

### SFI...Jan29.ipynb (old version)
- Superseded by October 2025 update
- Keeping old version would confuse users
- Updated version has improvements/corrections

### S1F...jan29.ipynb
- Too detailed for public sharing
- May contain exploratory code with sensitive data handling
- Simplified version (oct2025) is sufficient for reproducibility

### SI...jan29.ipynb
- Analyzes all ages, not just over-40
- Not used in the manuscript
- Would confuse readers about study population

---

## 🎯 Result

**GitHub repository will contain:**
1. ✅ One preprocessing notebook (oct2025 version)
2. ✅ One BERTopic analysis notebook (jan29 version)
3. ✅ All documentation files
4. ✅ Small result files (topics_info Excel files, disease_codes.xlsx)

**GitHub repository will NOT contain:**
1. ❌ Old/outdated notebooks
2. ❌ Large data files (*.pkl)
3. ❌ Trained models (700MB+ each)
4. ❌ Sensitive intermediate processing notebooks

---

**Last Updated:** 2025-10-18
**Changes Made:**
- Updated .gitignore to exclude 3 notebooks
- Force-included oct2025 preprocessing notebook
- Documented reasoning for exclusions
