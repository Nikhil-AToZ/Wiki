# Git
---
## Introduction

Git is a **distributed version control system** used to track changes in source code and other files.

It allows developers to maintain project history, create branches, experiment with features, and collaborate with other developers.

## Version Control

Version control records changes made to a project over time.

Git avoids the need to manually create multiple copies of a project and provides a structured way to return to previous versions.

## Git Repository

A Git repository is a project whose files and history are tracked by Git.

A repository can be created using:

```bash
git init
```

Git stores its internal information in the `.git` directory.

## Git Workflow

A common Git workflow is:

```text
Working Directory
       ↓
     git add
       ↓
Staging Area
       ↓
   git commit
       ↓
Repository
```

Changes are made in the working directory, selected changes are staged, and then committed to the repository.

## Basic Commands

Check the current state:

```bash
git status
```

Stage a file:

```bash
git add filename.py
```

Stage all changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add login functionality"
```

View commit history:

```bash
git log --oneline
```

## Branches

Branches allow developers to work on different features independently.

```bash
git switch -c feature-login
```

This creates and switches to a new branch.

Branches are useful because developers can work on features without immediately changing the main branch.

## Merging

A branch can be merged into another branch.

```bash
git switch main
git merge feature-login
```

Git combines the changes from the feature branch with the current branch.

## Merge Conflicts

A merge conflict happens when Git cannot automatically combine changes.

This commonly occurs when different branches modify the same part of a file.

The developer must resolve the conflict manually and then create a new commit.

## Remote Repositories

A remote repository is a repository stored somewhere outside the local computer.

A remote can be added using:

```bash
git remote add origin <repository-url>
```

The remote can be viewed using:

```bash
git remote -v
```

## GitHub and Git

Git and GitHub are different things.

**Git** is the version control system.

**GitHub** is a platform that hosts Git repositories and provides collaboration features.

```text
Git
 ├── Tracks changes
 ├── Creates commits
 ├── Manages branches
 └── Works locally

GitHub
 ├── Hosts repositories
 ├── Enables collaboration
 ├── Provides pull requests
 └── Provides issue tracking
```

## Push and Pull

`git push` uploads local commits to a remote repository.

```bash
git push origin main
```

`git pull` downloads changes from a remote repository and integrates them into the current branch.

```bash
git pull origin main
```

## Clone

An existing repository can be copied to a computer using:

```bash
git clone <repository-url>
```

## .gitignore

A `.gitignore` file tells Git which files should not be tracked.

Example:

```text
__pycache__/
*.pyc
.env
venv/
```

This is useful for excluding temporary files, secrets, and generated files.

## Advantages

- Tracks project history
- Supports branching and merging
- Makes collaboration easier
- Allows developers to experiment safely
- Works locally
- Widely used in professional development

## Limitations

- Git can be confusing for beginners.
- Merge conflicts sometimes require manual resolution.
- Advanced Git operations have a learning curve.
- Poor branch and commit management can make a repository difficult to maintain.

## Conclusion

Git is an essential tool for modern software development. It provides a reliable way to track changes, manage branches, maintain project history, and collaborate with other developers.

Understanding `clone`, `add`, `commit`, `push`, `pull`, `branch`, and `merge` provides a strong foundation for working with Git and GitHub.
