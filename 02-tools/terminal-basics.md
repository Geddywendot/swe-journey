# Terminal & Shell Fundamentals

The command line is the primary interface of professional software engineering. A deep comfort with POSIX shell semantics is essential.

---

## 1. Filesystem Navigation & Inspection

```bash
pwd              # Print working directory
ls -la           # Detailed listing including hidden dotfiles
cd path/to/dir   # Change directory
cd ..            # Move up one level
cd ~             # Move to user home directory
cd -             # Jump back to previous directory
```

---

## 2. File and Directory Operations

```bash
mkdir -p a/b/c   # Create nested directory tree
touch file.txt   # Create empty file or update timestamp
cp src.py dst.py # Copy file
cp -r src/ dst/  # Copy directory recursively
mv old.py new.py # Rename or move file
rm file.txt      # Remove file
rm -rf temp_dir/ # Recursively delete directory (use with caution)
cat file.txt     # Output file contents
head -n 20 file  # View first 20 lines
tail -n 20 file  # View last 20 lines
tail -f app.log  # Stream file changes in real time
```

---

## 3. Redirection and Streams

Every Unix process is initialized with three standard file descriptors:
- **`stdin` (0):** Standard input
- **`stdout` (1):** Standard output
- **`stderr` (2):** Standard error

```bash
# Redirect stdout to a file (overwrites)
command > output.txt

# Append stdout to a file
command >> output.txt

# Redirect stderr to a file
command 2> errors.txt

# Redirect both stdout and stderr to the same file
command > combined.log 2>&1

# Discard output entirely
command > /dev/null 2>&1
```

---

## 4. Pipelines & Text Processing

Pipes (`|`) connect the `stdout` of one process to the `stdin` of the next:

```bash
# Search for patterns inside files
grep -rn "TODO" src/

# Count lines, words, and characters
wc -l access.log

# Sort and deduplicate lines
sort access.log | uniq -c | sort -nr

# Extract columns from delimited text
cut -d ',' -f 1,3 users.csv

# Combine pipeline: Top 5 most frequent client IPs in access log
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -n 5
```

---

## 5. Process Management & Environment

```bash
# View active running processes
ps aux | grep python

# Monitor system resources and CPU/memory usage
top # or htop

# Terminate process gracefully (SIGTERM)
kill <PID>

# Force terminate process (SIGKILL)
kill -9 <PID>

# Inspect environment variables
printenv
echo $PATH
```
