# Final GitHub Upload List

**Repository:** https://github.com/skwgbobf/Multimorbidity_Bertopic
**Date:** 2025-10-18
**Status:** Ready for upload

---

## ✅ FILES THAT WILL BE UPLOADED

### 📓 Notebooks (2 files)

1. **Primary BERTopic Analysis (MANUSCRIPT VERSION)**
   - `1. Bertopic_over40/Shared_BERtopic_over40/Final_SIIF.MLM_BertTopic_all_100p 19year_over40_confirmed_option3_option2_dec07_dec13_gender_feb21_shared_afterre_july29F_Aug23.ipynb`
   - Size: 16MB
   - Purpose: FINAL manuscript analysis (168,529 patients, 19 female + 20 male topics)

2. **Preprocessing (Oct 2025 version)**
   - `SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb`
   - Size: 113KB
   - Purpose: BEHRT preprocessing workflow

### 📄 Documentation Files

- ✅ README.md
- ✅ USAGE_GUIDE.md
- ✅ DIRECTORY_STRUCTURE.md
- ✅ REPOSITORY_SUMMARY.md
- ✅ GIT_SETUP_GUIDE.md
- ✅ IMPLEMENTATION_ROADMAP.md
- ✅ GIT_FOCUSED_ACTION_PLAN.md
- ✅ NOTEBOOKS_INCLUDED_vs_EXCLUDED.md
- ✅ PRE_PUSH_VERIFICATION_CHECKLIST.md
- ✅ FINAL_UPLOAD_LIST.md (this file)

### 📦 Configuration

- ✅ requirements.txt
- ✅ .gitignore

### 📊 Small Data Files (MANUSCRIPT VERSION)

- ✅ disease_codes.xlsx (14KB)
- ✅ 1. Bertopic_over40/Shared_BERtopic_over40/100pall_19y_over40_option1_female_dec20_CTFIDF_aug23.xlsx (~10KB, 19 topics)
- ✅ 1. Bertopic_over40/Shared_BERtopic_over40/100pall_19y_over40_option1_male_dec20_CTFIDF_aug23.xlsx (~10KB, 20 topics)
- ✅ 1. Bertopic_over40/Shared_BERtopic_over40/Bertopic_over40_patientsID_aug23.xlsx (~2MB, 168,529 patients)

### 📁 Empty Directories (structure only)

- ✅ config/ (for future config.yaml)
- ✅ scripts/ (for future evaluation scripts)
- ✅ results/ (for future evaluation results)
- ✅ docs/ (for future detailed documentation)

---

## ❌ FILES THAT WILL NOT BE UPLOADED

### ❌ Notebooks (7 files excluded)

1. **S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb**
   - Reason: Too detailed/sensitive preprocessing

2. **SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb**
   - Reason: All-ages analysis (not used in manuscript)

3. **SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb**
   - Reason: Old version (superseded by oct2025)

4. **1. Bertopic_over40/SIIF.MLM_BertTopic...jan29.ipynb** (parent directory)
   - Reason: Old analysis version (superseded by Shared/Aug23 final version)

### ❌ Excel Files (3 files excluded)

5. **1. Bertopic_over40/topics_info_100p_over40_op1_female_dec20.xlsx**
   - Reason: Old format (superseded by CTFIDF format in Shared/)

6. **1. Bertopic_over40/topics_info_100p_over40_op1_male_dec20.xlsx**
   - Reason: Old format (superseded by CTFIDF format in Shared/)

7. **1. Bertopic_over40/topics_info_100p_over40_op1_male_dec20_2.xlsx**
   - Reason: Duplicate/old format

### ❌ Subdirectories (1 directory excluded)

8. **1. Bertopic_over40/new/**
   - Reason: Contains draft analyses and alternative options not used in manuscript

### ❌ Documentation Files (2 files excluded)

9. **LICENSE**
   - Reason: User requested exclusion

10. **PUBLICATION_CHECKLIST.md**
   - Reason: User requested exclusion (internal use only)

### ❌ Large Data Files (patient data - privacy)

- ❌ BFC.pkl (21.6MB)
- ❌ T20.pkl (119.6MB)
- ❌ DS.pkl (5.8KB)
- ❌ T20_BFC_BEHRT_group_data_BERTopic_over40_all.pkl (105MB)
- ❌ T20_BFC_BEHRT_group_data_sickFinal_mlm_op1_over40.pkl (52MB)
- ❌ T20_BFC_BEHRT_group_data_sickFinal_mlm_op2_over40.pkl (52MB)

### ❌ Trained Models (size - 1.4GB total)

- ❌ 1. Bertopic_over40/my_topics_model_100pall_19y_over40_option1_female_dec20/ (692MB)
- ❌ 1. Bertopic_over40/my_topics_model_100pall_19y_over40_option1_male_dec20/ (689MB)

---

## 📊 Upload Statistics

**Total files to upload:** ~25-30 files
**Total upload size:** ~25-35MB

**Breakdown:**
- Notebooks: ~18.1MB
- Documentation: ~0.5MB
- Data files: ~0.04MB
- Config: ~0.01MB

**Excluded size:** ~1.7GB (models + data files)

---

## 🔒 .gitignore Summary

### Excluded by pattern:
- All *.pkl files
- All *_model_*/ directories
- Results/ directories
- Data/ directories

### Explicitly excluded:
- S1F.BEHRT_datapreprocess_Aug19_over40_confirmed_nov16_jan29.ipynb
- SI.BEHRT_datapreprocess_Aug09_all_age_confirmed_nov16_dec07_jan29.ipynb
- SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29.ipynb
- LICENSE
- PUBLICATION_CHECKLIST.md

### Explicitly included (force override):
- README.md
- USAGE_GUIDE.md
- DIRECTORY_STRUCTURE.md
- requirements.txt
- .gitignore
- SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb
- disease_codes.xlsx
- topics_info_*.xlsx

---

## ✅ Pre-Upload Checklist

Before running `git push`:

- [ ] Verified .gitignore is committed
- [ ] Ran `git status` - no unwanted files appear
- [ ] Checked LICENSE is NOT in git status
- [ ] Checked S1F, SI, and old SFI notebooks are NOT in git status
- [ ] Checked oct2025 notebook IS in git status (if modified)
- [ ] Verified no *.pkl files in git status
- [ ] Verified no model directories in git status
- [ ] Ready to push

---

## 🚀 Quick Upload Commands

```bash
cd "C:\Data\Thesis_F\Multimorbidity_Support\GIT"

# Stage the updated .gitignore
git add .gitignore

# Stage documentation files
git add *.md

# Stage the oct2025 notebook (if modified)
git add SFI.BEHRT_datapreprocess_Aug19_over40_confirmed_nov29_Jan29_oct2025.ipynb

# Check status one more time
git status

# Commit
git commit -m "Update repository configuration: exclude LICENSE and old preprocessing notebooks"

# Push
git push origin main
```

---

## 🔍 Verification After Upload

Visit: https://github.com/skwgbobf/Multimorbidity_Bertopic

**Should see:**
- ✅ SFI...oct2025.ipynb
- ✅ SIIF.MLM_BertTopic...jan29.ipynb
- ✅ All .md documentation files
- ✅ requirements.txt
- ✅ .gitignore
- ✅ disease_codes.xlsx
- ✅ topics_info Excel files

**Should NOT see:**
- ❌ LICENSE
- ❌ PUBLICATION_CHECKLIST.md
- ❌ S1F.BEHRT_datapreprocess...jan29.ipynb
- ❌ SI.BEHRT_datapreprocess...jan29.ipynb
- ❌ SFI.BEHRT_datapreprocess...Jan29.ipynb (without oct2025)
- ❌ Any *.pkl files
- ❌ Any my_topics_model directories

---

**Configuration Complete:** ✅
**Last Updated:** 2025-10-18
**Ready to Upload:** Yes
