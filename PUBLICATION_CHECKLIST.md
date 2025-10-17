# Publication Checklist for Multimorbidity_Bertopic Repository

This checklist ensures your repository is ready for journal publication and public release.

## Pre-Publication Checklist

### 1. Documentation Completeness

- [x] **README.md** - Main project documentation created
  - Project overview and description
  - Installation instructions
  - Usage examples
  - Citation information
  - Contact details

- [x] **DIRECTORY_STRUCTURE.md** - Detailed file descriptions created
  - Complete file listing
  - Data schema documentation
  - File size information

- [x] **USAGE_GUIDE.md** - Step-by-step tutorial created
  - Prerequisites and installation
  - Data preprocessing workflow
  - BERTopic analysis workflow
  - Troubleshooting section

- [x] **GIT_SETUP_GUIDE.md** - Repository setup instructions created
  - Git initialization steps
  - GitHub repository creation
  - Git LFS configuration
  - Zenodo DOI instructions

- [x] **requirements.txt** - Python dependencies listed

- [x] **LICENSE** - MIT License with data usage notice

- [x] **.gitignore** - Git ignore rules configured

### 2. Code and Data Review

- [ ] **Review all notebooks** for sensitive information
  - Remove any hardcoded paths to personal directories
  - Remove any credentials or API keys
  - Ensure patient IDs are anonymized

- [ ] **Test notebooks** end-to-end
  - Verify preprocessing notebook runs successfully
  - Verify BERTopic notebook runs successfully
  - Check for any missing dependencies

- [ ] **Verify data files**
  - All pickle files are present and loadable
  - disease_codes.xlsx is readable
  - Topic result Excel files are included

- [ ] **Update file paths** in notebooks
  - Replace absolute paths with relative paths
  - Use generic placeholders for data directories
  - Add comments explaining path configuration

### 3. Ethics and Privacy

- [ ] **IRB Approval** obtained (if required)
  - Document IRB approval number in README
  - Include ethics statement in manuscript

- [ ] **Data Anonymization** verified
  - Confirm all patient IDs are anonymized
  - No dates of birth or identifying information
  - Comply with HIPAA/GDPR requirements

- [ ] **Informed Consent** addressed
  - Ensure data usage complies with consent agreements
  - Document any data use restrictions

### 4. Author and Institution Information

- [ ] **Update placeholder information** in all files:
  - Replace `[Your Name]` with actual author names
  - Replace `[Your Institution]` with institution name
  - Replace `[your.email@institution.edu]` with contact email
  - Replace `[Journal Name]` with target journal

- [ ] **Co-author approval**
  - All co-authors have reviewed the repository
  - All co-authors approve public release
  - Contributor acknowledgments are accurate

### 5. Repository Configuration

- [ ] **Choose repository name**: `Multimorbidity_Bertopic`

- [ ] **Repository visibility**: Start as Private, then make Public

- [ ] **Repository description**:
  > "Multimorbidity pattern discovery using BERTopic in patients aged 40 and above - Code and analysis for [Journal Name] publication"

- [ ] **Topics/Tags** (on GitHub):
  - multimorbidity
  - bertopic
  - electronic-health-records
  - topic-modeling
  - healthcare-analytics
  - behrt
  - comorbidity

### 6. Version Control Setup

- [ ] **Initialize Git repository**
  ```bash
  cd "C:\Data\Thesis_F\Multimorbidity_Support\GIT"
  git init
  ```

- [ ] **Install and configure Git LFS**
  ```bash
  git lfs install
  git lfs track "*.pkl"
  git lfs track "*.pickle"
  git lfs track "my_topics_model_*/**"
  ```

- [ ] **Create .gitattributes file** (auto-created by git lfs track)

- [ ] **Create initial commit**
  ```bash
  git add .
  git commit -m "Initial commit: Multimorbidity BERTopic analysis"
  ```

### 7. GitHub Repository Creation

- [ ] **Create GitHub repository**
  - Go to https://github.com/new
  - Name: `Multimorbidity_Bertopic`
  - Visibility: Private (initially)
  - Do NOT initialize with README

- [ ] **Link local to GitHub**
  ```bash
  git remote add origin https://github.com/yourusername/Multimorbidity_Bertopic.git
  git branch -M main
  git push -u origin main
  ```

- [ ] **Verify upload**
  - Check all files are present on GitHub
  - Verify Git LFS files show "Stored with Git LFS" badge

### 8. Create Release for Publication

- [ ] **Create GitHub Release**
  - Tag: `v1.0.0`
  - Title: "Publication Release - [Journal Name]"
  - Description: Include abstract and key findings
  - Attach any supplementary files

### 9. Obtain DOI from Zenodo

- [ ] **Link GitHub to Zenodo**
  - Go to https://zenodo.org/account/settings/github/
  - Authorize and enable repository

- [ ] **Create release** (triggers Zenodo archiving)

- [ ] **Get DOI** from Zenodo

- [ ] **Add DOI badge** to README.md
  ```markdown
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXX)
  ```

### 10. Make Repository Public

**Only after completing all above steps!**

- [ ] **Final review** of all files

- [ ] **Make repository public**
  - Settings → Danger Zone → Change visibility → Public

- [ ] **Announce repository**
  - Add repository link to manuscript
  - Include in supplementary materials

## During Manuscript Preparation

### Code Availability Statement

Include in your manuscript:

```
Code Availability

All code for data preprocessing and BERTopic analysis is publicly available
on GitHub at https://github.com/yourusername/Multimorbidity_Bertopic and
archived on Zenodo with DOI: 10.5281/zenodo.XXXXXX.

The code is released under the MIT License and includes comprehensive
documentation, example usage, and installation instructions.
```

### Data Availability Statement

```
Data Availability

Due to patient privacy regulations, the raw electronic health record data
cannot be publicly shared. The code repository includes:
- Complete preprocessing and analysis pipeline
- Disease code definitions
- Aggregated topic modeling results
- Synthetic example data for testing

Researchers with appropriate ethical approval may request access to
anonymized datasets by contacting [contact person] at [institution].
```

### Citation Format

Provide this in your repository README:

```bibtex
@article{author2024multimorbidity,
  title={Multimorbidity Pattern Discovery using BERTopic in Patients Aged 40 and Above},
  author={Author, First and Author, Second},
  journal={Journal Name},
  year={2024},
  volume={XX},
  pages={XXX-XXX},
  doi={10.XXXX/journal.XXXX}
}

@software{author2024multimorbidity_code,
  author={Author, First and Author, Second},
  title={Multimorbidity BERTopic Analysis Code},
  year={2024},
  publisher={Zenodo},
  version={v1.0.0},
  doi={10.5281/zenodo.XXXXXX},
  url={https://github.com/yourusername/Multimorbidity_Bertopic}
}
```

## Post-Publication Maintenance

### After Paper Acceptance

- [ ] **Update README** with publication details
  - Add published paper DOI
  - Update citation information
  - Link to published article

- [ ] **Create new release** (if code changed during review)
  - Tag: `v1.0.1` or `v1.1.0`
  - Description: "Updated for final publication"

- [ ] **Monitor repository**
  - Respond to issues and questions
  - Fix any bugs reported
  - Update documentation as needed

### Long-term Maintenance

- [ ] **Keep dependencies updated**
  - Update requirements.txt periodically
  - Test with new Python versions
  - Document compatibility issues

- [ ] **Address community contributions**
  - Review pull requests
  - Acknowledge contributors
  - Maintain code quality

## Common Mistakes to Avoid

1. **Don't commit before review**
   - Always review files before initial commit
   - Use `git status` and `git diff` to check what will be committed

2. **Don't expose sensitive data**
   - Never commit patient data, even anonymized IDs
   - Remove credentials, API keys, file paths

3. **Don't skip Git LFS**
   - Large files (>100MB) must use Git LFS
   - Set up LFS before first commit

4. **Don't forget documentation**
   - Code without documentation is hard to use
   - Future you will thank present you

5. **Don't make public too early**
   - Keep private until manuscript is accepted
   - Reviewers may discover repository prematurely

6. **Don't ignore licensing**
   - Always include a LICENSE file
   - Choose appropriate license for your needs

## Troubleshooting

### Large Files Rejected by GitHub

```bash
# Remove from cache
git rm --cached large_file.pkl

# Track with LFS
git lfs track "large_file.pkl"
git add .gitattributes
git add large_file.pkl
git commit -m "Track large file with LFS"
```

### Need to Remove Committed Sensitive Data

```bash
# CAUTION: This rewrites history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/file" \
  --prune-empty --tag-name-filter cat -- --all

git push --force  # Only if repository is private and fresh
```

Better: Delete repository and start over with proper .gitignore.

### Notebook Output Too Large

Option 1: Clear outputs before committing
```bash
jupyter nbconvert --clear-output --inplace notebook.ipynb
```

Option 2: Use nbstripout to auto-clear
```bash
pip install nbstripout
nbstripout --install
```

## Resources

- **Git Documentation**: https://git-scm.com/doc
- **GitHub Guides**: https://guides.github.com/
- **Git LFS**: https://git-lfs.github.com/
- **Zenodo**: https://zenodo.org/
- **Choosing a License**: https://choosealicense.com/
- **Journal Policies**: Check your target journal's code sharing policy

## Contact for Help

- **Technical Issues**: [your.email@institution.edu]
- **Data Access Requests**: [data.custodian@institution.edu]
- **Collaboration Inquiries**: [pi.email@institution.edu]

## Final Notes

This repository represents months of research work. Take time to:
- Organize it properly
- Document it thoroughly
- Share it responsibly
- Maintain it actively

Good documentation and code sharing advance science and benefit the community.

**Good luck with your publication!**
