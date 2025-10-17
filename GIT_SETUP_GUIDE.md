# Git Repository Setup Guide

This guide will help you initialize and publish your Multimorbidity_Bertopic repository for journal publication.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Initial Git Setup](#initial-git-setup)
3. [Preparing Large Files with Git LFS](#preparing-large-files-with-git-lfs)
4. [Creating the GitHub Repository](#creating-the-github-repository)
5. [First Commit and Push](#first-commit-and-push)
6. [Repository Organization](#repository-organization)
7. [Making the Repository Public](#making-the-repository-public)
8. [Getting a DOI with Zenodo](#getting-a-doi-with-zenodo)

## Prerequisites

### 1. Install Git

**Windows:**
- Download from: https://git-scm.com/download/win
- Run installer with default options

**macOS:**
```bash
brew install git
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install git
```

### 2. Install Git LFS (Large File Storage)

Git LFS is essential for handling large data files (>100MB).

**Windows:**
- Download from: https://git-lfs.github.com/
- Run installer

**macOS:**
```bash
brew install git-lfs
```

**Linux:**
```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

**Initialize Git LFS:**
```bash
git lfs install
```

### 3. Create GitHub Account

If you don't have one:
1. Go to https://github.com
2. Sign up for a free account
3. Verify your email address

## Initial Git Setup

### 1. Configure Git

```bash
# Set your name and email (will appear in commits)
git config --global user.name "Your Name"
git config --global user.email "your.email@institution.edu"

# Verify configuration
git config --list
```

### 2. Navigate to Your Project Directory

```bash
cd "C:\Data\Thesis_F\Multimorbidity_Support\GIT"
# or on Linux/Mac:
# cd /path/to/Multimorbidity_Support/GIT
```

### 3. Initialize Git Repository

```bash
# Initialize git repository
git init

# Check status
git status
```

You should see all your files as "untracked".

## Preparing Large Files with Git LFS

### 1. Configure Git LFS for Large Files

```bash
# Track pickle files
git lfs track "*.pkl"
git lfs track "*.pickle"

# Track BERTopic model directories
git lfs track "my_topics_model_*/**"

# Track large CSV files (if you decide to include them)
# git lfs track "*.csv"

# Verify LFS tracking
cat .gitattributes
```

This creates a `.gitattributes` file that tells Git LFS which files to manage.

### 2. Add .gitattributes to Git

```bash
git add .gitattributes
```

### 3. Check Which Files Will Be Tracked by LFS

```bash
git lfs ls-files
```

## Creating the GitHub Repository

### Option A: Via GitHub Website (Recommended for Beginners)

1. Go to https://github.com
2. Click the "+" icon in top-right corner
3. Select "New repository"
4. Fill in:
   - **Repository name:** `Multimorbidity_Bertopic`
   - **Description:** "Multimorbidity pattern discovery using BERTopic in patients aged 40 and above"
   - **Visibility:** Start with "Private" (change to public later)
   - **Do NOT** initialize with README (you already have one)
5. Click "Create repository"
6. Copy the repository URL (e.g., `https://github.com/yourusername/Multimorbidity_Bertopic.git`)

### Option B: Via Command Line (Advanced)

```bash
# Install GitHub CLI first
# Windows: Download from https://cli.github.com/
# macOS: brew install gh
# Linux: See https://github.com/cli/cli/blob/trunk/docs/install_linux.md

# Login to GitHub
gh auth login

# Create repository
gh repo create Multimorbidity_Bertopic --private --source=. --remote=origin
```

## First Commit and Push

### 1. Link Local Repository to GitHub

If you created the repo via website:

```bash
git remote add origin https://github.com/yourusername/Multimorbidity_Bertopic.git

# Verify remote
git remote -v
```

### 2. Stage Files for Commit

**Important:** Review `.gitignore` to ensure sensitive data is excluded.

```bash
# Add all files (respecting .gitignore)
git add .

# Check what will be committed
git status
```

### 3. Create Initial Commit

```bash
git commit -m "Initial commit: Multimorbidity BERTopic analysis code and documentation

- Add BEHRT preprocessing notebooks
- Add BERTopic analysis notebook
- Add comprehensive documentation (README, USAGE_GUIDE, DIRECTORY_STRUCTURE)
- Add requirements.txt and .gitignore
- Include disease codes and topic analysis results
- Add preprocessed datasets and trained models (via Git LFS)"
```

### 4. Push to GitHub

```bash
# Push to main branch
git push -u origin main

# If you get an error about 'master' vs 'main':
git branch -M main
git push -u origin main
```

**Note:** Pushing large files may take time. Git LFS will upload large files to LFS storage.

### 5. Verify Upload

1. Go to your GitHub repository in a web browser
2. Check that all files are present
3. Large files tracked by LFS will show "Stored with Git LFS" badge

## Repository Organization

### Recommended Branch Structure

For publication, a simple structure is best:

```
main (default branch)
  ├── All stable, documented code
  └── Ready for publication
```

For ongoing development:

```bash
# Create development branch
git checkout -b development

# Work on development branch
# ...make changes...

# Commit changes
git add .
git commit -m "Description of changes"

# Push development branch
git push -u origin development

# When ready, merge to main via pull request on GitHub
```

### Adding a Release for Publication

When ready to publish:

1. Go to your GitHub repository
2. Click "Releases" (right sidebar)
3. Click "Create a new release"
4. Fill in:
   - **Tag version:** `v1.0.0`
   - **Release title:** "Multimorbidity BERTopic Analysis - Publication Release"
   - **Description:** Brief description and DOI (if available)
5. Click "Publish release"

This creates a permanent snapshot that can be cited.

## Making the Repository Public

### Before Making Public

**Checklist:**
- [ ] All patient data is anonymized
- [ ] No credentials or API keys in code
- [ ] IRB approval obtained (if required)
- [ ] Co-authors have reviewed and approved
- [ ] Documentation is complete and accurate
- [ ] License file is included
- [ ] Citation information is provided

### Steps to Make Public

1. Go to repository on GitHub
2. Click "Settings" tab
3. Scroll to "Danger Zone"
4. Click "Change visibility"
5. Select "Make public"
6. Type repository name to confirm
7. Click "I understand, make this repository public"

## Getting a DOI with Zenodo

A DOI (Digital Object Identifier) makes your code citeable in academic papers.

### 1. Create Zenodo Account

1. Go to https://zenodo.org
2. Sign up (can use GitHub account)
3. Verify email

### 2. Link GitHub to Zenodo

1. Log in to Zenodo
2. Go to https://zenodo.org/account/settings/github/
3. Click "Connect to GitHub"
4. Authorize Zenodo
5. Toggle ON your `Multimorbidity_Bertopic` repository

### 3. Create a Release (Triggers Zenodo)

On GitHub:
1. Go to your repository
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0`
4. Title: "Publication Release - Multimorbidity BERTopic Analysis"
5. Description: Include abstract, methods summary
6. Click "Publish release"

Zenodo will automatically:
- Archive the release
- Generate a DOI
- Create a permanent record

### 4. Get Your DOI

1. Go to Zenodo
2. Navigate to "Upload" → "Deposits"
3. Find your repository
4. Copy the DOI (e.g., `10.5281/zenodo.1234567`)

### 5. Add DOI Badge to README

Add to your README.md:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
```

Then commit and push:

```bash
git add README.md
git commit -m "Add Zenodo DOI badge"
git push
```

## Maintenance and Updates

### Making Updates After Publication

```bash
# Make changes to files
# ...edit files...

# Stage changes
git add .

# Commit with descriptive message
git commit -m "Fix: Correct disease code mapping in preprocessing"

# Push to GitHub
git push

# For significant updates, create a new release (v1.0.1, v1.1.0, etc.)
```

### Creating a New Release

For bug fixes or minor updates:

```bash
# Tag: v1.0.1 (patch)
# For new features: v1.1.0 (minor)
# For major changes: v2.0.0 (major)
```

## Common Git Commands Reference

```bash
# Check status of files
git status

# Add files to staging
git add filename.py
git add .  # Add all changed files

# Commit staged changes
git commit -m "Commit message"

# Push to GitHub
git push

# Pull latest changes from GitHub
git pull

# View commit history
git log
git log --oneline  # Condensed view

# Undo uncommitted changes
git checkout -- filename.py

# View differences
git diff filename.py

# Create new branch
git checkout -b new-branch-name

# Switch branches
git checkout main

# Merge branch
git merge development

# View remote repositories
git remote -v

# Clone repository
git clone https://github.com/yourusername/Multimorbidity_Bertopic.git
```

## Troubleshooting

### Large File Upload Fails

**Error:** `file size exceeds 100 MB`

**Solution:**
```bash
# Ensure Git LFS is installed
git lfs install

# Track the large file
git lfs track "large_file.pkl"

# Add .gitattributes
git add .gitattributes

# Remove file from git cache
git rm --cached large_file.pkl

# Re-add with LFS
git add large_file.pkl
git commit -m "Track large file with LFS"
git push
```

### Authentication Issues

**Error:** `Authentication failed`

**Solution:**
```bash
# Use Personal Access Token (PAT) instead of password
# Generate PAT at: https://github.com/settings/tokens

# On Windows, use Git Credential Manager
# It will prompt for credentials and save them

# On Mac/Linux, cache credentials
git config --global credential.helper cache
```

### Push Rejected

**Error:** `Updates were rejected`

**Solution:**
```bash
# Pull latest changes first
git pull origin main

# Resolve any conflicts
# Then push again
git push
```

### Remove Sensitive Data

If you accidentally committed sensitive data:

```bash
# Remove file from git history (CAREFUL!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch path/to/sensitive_file" \
  --prune-empty --tag-name-filter cat -- --all

# Force push (DANGEROUS - only if repository is private and you're sure)
git push --force
```

Better: Delete repository, fix .gitignore, and start fresh.

## Best Practices for Academic Repositories

1. **Clear Documentation:**
   - Comprehensive README
   - Usage examples
   - Citation information

2. **Reproducibility:**
   - Pin dependency versions (requirements.txt)
   - Document random seeds
   - Include environment details

3. **Data Privacy:**
   - Never commit real patient data
   - Use synthetic/anonymized data for examples
   - Include ethics approval information

4. **Version Control:**
   - Use semantic versioning (v1.0.0)
   - Tag releases for publications
   - Maintain changelog

5. **Code Quality:**
   - Comment your code
   - Use meaningful variable names
   - Include docstrings

6. **Licensing:**
   - Include LICENSE file
   - Choose appropriate license (MIT, Apache, GPL)

7. **Collaboration:**
   - Use issues for bug reports
   - Accept pull requests if open to contributions
   - Acknowledge contributors

## Journal Submission Checklist

Before submitting your paper:

- [ ] Repository is public on GitHub
- [ ] All code is documented and runnable
- [ ] README includes installation and usage instructions
- [ ] requirements.txt is complete and tested
- [ ] Data is anonymized (or synthetic examples provided)
- [ ] License file is included
- [ ] Release has been created (v1.0.0)
- [ ] DOI obtained from Zenodo
- [ ] DOI badge added to README
- [ ] Repository URL and DOI included in manuscript
- [ ] Code availability statement in paper references GitHub and Zenodo

## Getting Help

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Git LFS:** https://git-lfs.github.com/
- **Zenodo Help:** https://help.zenodo.org/

## Contact

For questions about this repository:
- **Email:** [your.email@institution.edu]
- **GitHub Issues:** https://github.com/yourusername/Multimorbidity_Bertopic/issues
