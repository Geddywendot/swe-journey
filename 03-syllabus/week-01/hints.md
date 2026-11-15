# Week 01 Hints

> **Rule:** Attempt the exercise for at least 30 minutes before reading Hint 1. Wait an additional 15 minutes before reading Hint 2 or 3.

---

## Exercise 1.1: Log Extraction Pipeline with Unix Utilities

### Hint Level 1 (Nudge)
Look closely at the structure of standard combined access logs. The client IP is usually field 1, and the HTTP status code is usually field 9.

### Hint Level 2 (Concept Name)
Use `awk` to filter lines where the status code matches `"200"`, print the IP address, then chain with `sort | uniq -c | sort -nr`.

### Hint Level 3 (Direction)
In bash, `$1` holds the first CLI argument. You can test `if [ -n "$1" ]; then input_stream="$1"; else input_stream="/dev/stdin"; fi`. Pass this stream into your `awk` expression, pipe to `sort` (required before `uniq`), pipe to `uniq -c` to count occurrences, and finally pipe to `head -n 5`.

---

## Exercise 1.2: Debug This — Rescuing a Broken Git State

### Hint Level 1 (Nudge)
Git never permanently destroys commits immediately when you detach or change branches; they still exist in the repository's internal reference log.

### Hint Level 2 (Concept Name)
Run `git reflog` to locate the exact commit SHA of the hotfix commit made while detached.

### Hint Level 3 (Direction)
Once you find the SHA in `git reflog`, do not try to cherry-pick blind. Create a branch pointer directly at that hash using `git branch hotfix/critical <SHA>`. Then switch back to `main` with `git switch main` and run `git merge hotfix/critical`.

---

## Exercise 1.3: Simulating and Resolving 3-Way Merge Conflicts

### Hint Level 1 (Nudge)
Git detects conflicts when two branches modify the exact same line in a file since their common ancestor.

### Hint Level 2 (Concept Name)
The section between `<<<<<<< HEAD` and `=======` is the version in your current branch. The section between `=======` and `>>>>>>> <branch-name>` is the incoming version.

### Hint Level 3 (Direction)
To resolve, edit the file in your text editor, remove all lines containing `<<<<<<<`, `=======`, and `>>>>>>>`, retain the reconciled business logic, stage the file with `git add <filename>`, and finalize with `git commit`.
