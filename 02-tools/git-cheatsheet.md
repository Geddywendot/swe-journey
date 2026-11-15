# Git Command Reference & Mental Model

Git is not merely a file backup utility; it is a content-addressable directed acyclic graph (DAG) of object snapshots.

---

## 1. Inspecting State & History

```bash
# Check working tree and staging area status
git status

# View differences between working tree and staging area
git diff

# View differences between staging area and HEAD (last commit)
git diff --staged

# Clean, single-line log showing graph structure
git log --oneline --graph --decorate --all

# Inspect details of a specific commit or object
git show <commit-hash>
```

---

## 2. Branching & Context Switching

```bash
# Create and switch to a new branch
git checkout -b <branch-name>
# or modern syntax:
git switch -c <branch-name>

# List all local branches
git branch

# Switch to an existing branch
git switch <branch-name>

# Delete a merged branch
git branch -d <branch-name>

# Force delete an unmerged branch
git branch -D <branch-name>
```

---

## 3. Staging and Committing

```bash
# Stage specific file
git add path/to/file.py

# Stage modified and deleted tracked files (avoid adding untracked junk)
git add -u

# Commit with a descriptive conventional message
git commit -m "feat(auth): validate JWT expiration timestamp"

# Amend the most recent commit (DO NOT use on pushed public commits)
git commit --amend
```

---

## 4. Undoing Mistakes Safely

### Working Tree (Unstaged Changes)
```bash
# Discard modifications to a file in working tree
git restore path/to/file.py
```

### Staging Area
```bash
# Unstage a file, keeping modifications in working tree
git restore --staged path/to/file.py
```

### Commits
```bash
# Soft reset: undo commit, keep changes staged
git reset --soft HEAD~1

# Mixed reset (default): undo commit and unstage changes
git reset HEAD~1

# Create a new commit that inverts an earlier commit (safe for shared branches)
git revert <commit-hash>
```

---

## 5. Working with Remotes

```bash
# Inspect configured remotes
git remote -v

# Fetch latest refs from remote without merging
git fetch origin

# Pull and rebase local commits on top of upstream
git pull --rebase origin main

# Push branch and set upstream tracking
git push -u origin <branch-name>
```
