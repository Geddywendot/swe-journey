# Quiz 01

Test your conceptual understanding of Git mechanics and Unix streams. Record your answers before consulting your learning partner or answer key.

1. In the Unix pipeline `grep "ERROR" app.log | sort | uniq -c`, why must `sort` be executed prior to `uniq -c`?
   a) `uniq` consumes more memory if the input is unsorted.  
   b) `uniq` only detects adjacent duplicate lines in the stream.  
   c) `sort` strips whitespace required for `uniq` to parse tokens.  
   d) POSIX pipelines require alphabetic ordering for all data streams.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

2. If you modify a single file in your repository and run `git add`, what object is created inside `.git/objects`?
   a) A commit object containing the file metadata.  
   b) A tree object containing the directory listing.  
   c) A blob object containing the compressed contents of the modified file.  
   d) A reflog entry recording the modification.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

3. What physically represents a local branch named `feature/login` on your filesystem?
   a) A directory copy of your entire working tree under `.git/branches/feature/login`.  
   b) A 41-byte text file at `.git/refs/heads/feature/login` containing the SHA-1/SHA-256 hash of its tip commit.  
   c) A binary database table entry in SQLite.  
   d) A compressed zip archive in `.git/objects`.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

4. What happens when your repository enters a "detached HEAD" state?
   a) Git deletes all uncommitted files in your working directory.  
   b) The `.git` index is corrupted and must be re-cloned.  
   c) The `HEAD` pointer references a specific commit hash rather than a named branch ref.  
   d) You can no longer run `git diff` or `git status`.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

5. Under what condition can Git perform a "fast-forward" merge?
   a) When the target branch has no commits ahead of the common ancestor.  
   b) When both branches have conflicting edits on different lines.  
   c) Only when merging via GitHub pull requests with administrative privileges.  
   d) Whenever both branches have identical commit timestamps.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

6. Why is running `git rebase` on a branch that has already been pushed to a shared remote considered dangerous?
   a) It deletes the remote branch permanently.  
   b) It rewrites the commit hashes, causing divergent histories and merge confusion for teammates.  
   c) It converts all blob objects to read-only mode.  
   d) Git's internal garbage collector immediately destroys unreferenced tags.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

7. What is the fundamental difference between standard output (`stdout`, file descriptor 1) and standard error (`stderr`, file descriptor 2)?
   a) `stdout` is buffered and intended for program data; `stderr` is unbuffered and intended for diagnostic/error messages so they are not lost in downstream pipes.  
   b) `stdout` can only write text; `stderr` can only write binary.  
   c) `stderr` automatically terminates the process upon writing.  
   d) `stdout` cannot be redirected to a file.  
   *(Answer key: `instructor-keys/quiz-01.md`)*

8. How does Git determine that a merge conflict exists between two branches?
   a) By comparing file size differences across both commits.  
   b) By comparing both branch tips against their common merge base ancestor and detecting divergent edits to the same lines.  
   c) By checking if both authors have the same Git email address.  
   d) By checking whether the files were edited on the same calendar day.  
   *(Answer key: `instructor-keys/quiz-01.md`)*
