# Repository Setup Instructions

Follow these steps to get your GitHub repository set up:

## Step 1: Initialize Git Repository (if not already done)

```bash
git init
```

## Step 2: Add Your Files

```bash
git add .
git commit -m "Initial commit"
```

## Step 3: Create Repository on GitHub

1. Go to https://github.com
2. Click the "+" icon in the top right
3. Select "New repository"
4. Fill in:
   - Repository name
   - Description (optional)
   - Choose Public or Private
   - Do NOT initialize with README (you already have one)
5. Click "Create repository"

## Step 4: Connect Local Repository to GitHub

GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 5: Protect Your Main Branch (Recommended)

On GitHub:
1. Go to your repository
2. Click "Settings"
3. Click "Branches" in the left sidebar
4. Click "Add rule"
5. In "Branch name pattern", type: main
6. Check these options:
   - "Require pull request reviews before merging"
   - "Require status checks to pass before merging"
7. Click "Create"

This prevents direct pushes to main and requires pull requests.

## Step 6: Share with Your Team

Send your team members:
1. The repository URL
2. The README.md instructions
3. Make sure they have access (add them as collaborators in Settings > Collaborators)

## Step 7: Create a Virtual Environment Template

Each developer should run:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Common Commands Cheat Sheet

```bash
# Check status
git status

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature/my-feature

# Stage changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push branch
git push origin branch-name

# Switch branches
git checkout branch-name

# List all branches
git branch -a
```
