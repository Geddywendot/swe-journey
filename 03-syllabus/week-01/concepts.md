# Week 01 Concepts

Master these 6 foundational ideas. For each concept, practice explaining it aloud in your own words.

---

### 1. The Unix Philosophy: Small Tools Composed via Streams
- **Plain words:** Programs should do one thing well and communicate via simple text streams (`stdin`, `stdout`, `stderr`). By chaining small tools (`cat`, `grep`, `sort`, `awk`) with pipes (`|`), you can solve complex processing tasks without writing custom programs.
- **Explain it back prompt:** *"Explain how a pipeline like `cat access.log | grep 404 | wc -l` works under the hood in terms of operating system file descriptors."*

### 2. The Git Object Model (Blobs, Trees, Commits)
- **Plain words:** Git is not a list of file diffs. It is a content-addressable key-value database stored in `.git/objects`. A **blob** stores raw file content; a **tree** represents a directory listing pointing to blobs and subtrees with file modes; a **commit** is an immutable snapshot pointing to a top-level tree, parent commit(s), author metadata, and a log message.
- **Explain it back prompt:** *"If you edit one single character in a 10MB file and commit it, what new objects are created in `.git/objects` and what happens to the unchanged files?"*

### 3. Branches are Lightweight Movable Pointers
- **Plain words:** In Git, a branch is not a copy of your codebase. It is literally a 41-byte text file in `.git/refs/heads/<branch-name>` containing the 40-character SHA hash of the latest commit. Creating a branch takes microseconds and costs virtually zero disk space.
- **Explain it back prompt:** *"What is `HEAD` and how does Git know which branch you currently have checked out?"*

### 4. Detached HEAD State
- **Plain words:** A detached HEAD occurs when `HEAD` points directly to a specific commit SHA rather than to a named branch reference. Any new commits made while in this state will become orphaned (lost to garbage collection) if you switch branches without naming a new branch pointer.
- **Explain it back prompt:** *"How do you safely rescue work committed while in a detached HEAD state?"*

### 5. Fast-Forward Merge vs. Three-Way Merge
- **Plain words:** A fast-forward merge simply moves the branch pointer forward because there was no divergent history. A three-way merge occurs when both branches have new commits; Git finds the common ancestor commit and synthesizes a new merge commit combining both lines of history.
- **Explain it back prompt:** *"Why can a fast-forward merge never produce a merge conflict, while a 3-way merge can?"*

### 6. Merge vs. Rebase Trade-offs
- **Plain words:** Merging preserves the exact historical record and sequence of commits, but can result in cluttered history graphs. Rebasing re-writes project history by replaying local commits on top of the target branch, producing a clean, linear history at the risk of rewriting shared public commits.
- **Explain it back prompt:** *"What is the golden rule of rebasing, and what disasters happen when you rebase a shared remote branch?"*
