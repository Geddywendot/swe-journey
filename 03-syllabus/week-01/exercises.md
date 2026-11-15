# Week 01 Exercises

Complete all Silver exercises to pass the week. Gold exercises are optional stretch challenges.

---

## Exercise 1.1: Log Extraction Pipeline with Unix Utilities

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Given a raw Apache/Nginx web server access log, write a reusable POSIX shell script `scripts/top_ips.sh` that extracts the top 5 most frequent client IP addresses along with their request counts, formatted in descending order.

**Acceptance criteria:**
- [ ] Accepts a log file path as an argument `$1`, or reads from `stdin` if no file argument is passed.
- [ ] Filters out non-200 HTTP status responses before counting.
- [ ] Outputs lines formatted cleanly as: `<count> <ip-address>`.
- [ ] Handles missing files gracefully with an informative error message to `stderr` and non-zero exit code.

**Rules:** AI off. Use standard utilities (`awk`, `grep`, `sort`, `uniq`, `head`). Test with edge cases (empty file, file with only 404s).  
**Hints:** See `hints.md` section 1.1

---

## Exercise 1.2: Debug This — Rescuing a Broken Git State

**Type:** silver ("debug this")  
**Time box:** 60–90 min  
**Task:** A developer ran into trouble while trying to inspect an old release. They executed commands that left their repository in a confusing state with orphaned commits and unresolved conflict markers.

Here is the setup script that creates the broken repository state:
```bash
mkdir -p /tmp/broken-git && cd /tmp/broken-git
git init
echo "version 1.0" > app.txt && git add app.txt && git commit -m "feat: release 1.0"
echo "feature alpha" >> app.txt && git commit -am "feat: add alpha"
COMMIT_ALPHA=$(git rev-parse HEAD)
git checkout HEAD~1
echo "hotfix critical" >> app.txt && git commit -am "fix: critical hotfix"
# The developer now finds themselves detached, cannot switch to main cleanly, and thinks their work is deleted!
```

**Acceptance criteria:**
- [ ] Identify the detached commit hash containing the critical hotfix.
- [ ] Safely create a formal branch `hotfix/critical` from the detached commit without losing any commits.
- [ ] Merge `hotfix/critical` into `main`, resolving any conflicts cleanly.
- [ ] Verify that `git log --graph --oneline --all` shows a clean history with all work preserved.

**Rules:** Do not delete the `.git` directory to "start over". Use `git branch`, `git reflog`, and `git merge`.  
**Hints:** See `hints.md` section 1.2

---

## Exercise 1.3: Simulating and Resolving 3-Way Merge Conflicts

**Type:** silver  
**Time box:** 60–90 min  
**Task:** Create a reproduction sandbox script `scripts/reproduce_conflict.sh` that initializes a git repository, branches off `main` to `feature/payment-gateway`, alters the same configuration block in both branches with differing logic, and attempts a merge to intentionally trigger a conflict. Then write a documented resolution guide.

**Acceptance criteria:**
- [ ] Script generates a conflicting state deterministically.
- [ ] Conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) are inspected and explained line-by-line.
- [ ] Resolve the conflict by combining valid changes from both branches.
- [ ] Complete the merge commit and verify tree integrity.

**Rules:** Resolve manually without graphical merge tools.  
**Hints:** See `hints.md` section 1.3

---

## Exercise 1.4: Low-Level Git Plumbing Exploration

**Type:** gold (stretch)  
**Time box:** 120–180 min  
**Task:** Create a complete, valid Git commit from scratch without ever using porcelain commands (`git add` or `git commit`). Use only low-level plumbing commands: `git hash-object`, `git mktree`, `git commit-tree`, and update `.git/refs/heads/custom-branch`.

**Acceptance criteria:**
- [ ] Hash a text file into `.git/objects` using `git hash-object -w`.
- [ ] Construct a tree object using `git write-tree` or `git mktree`.
- [ ] Create a commit object pointing to the tree with `git commit-tree`.
- [ ] Update branch ref to point to the commit using `git update-ref`.
- [ ] `git log` and `git checkout` recognize the commit seamlessly.

**Rules:** No hints provided for gold stretch exercises.
