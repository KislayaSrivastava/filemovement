#  FileMovement — Automated File Search & Copy Utility

A Python script to **search for files by type** within a specified directory on Windows and **copy them to a destination folder**. A practical utility to simplify tasks like organizing files, backups, and categorization.

---

##  Features

- Search desktop (or any directory) recursively for files matching a **specified extension** (e.g., `.pdf`, `.jpg`, `.xlsx`).
- Copy all found files to a **user-defined destination folder**.
- Customizable via **simple command-line arguments**.
- Lightweight, no external dependencies—pure Python.

---

##  Tech Stack

- Python 3.x  
- Built-in modules: `os`, `shutil`, `argparse`

---

##  Usage Instructions

### Prerequisites

- Python 3.x installed on Windows systems.

### Command-Line Usage

```bash
python filemovement.py --source "C:\Users\YourName\Desktop" --ext ".pdf" --dest "D:\FileBackup\PDFs"
```

## What I learnt

1. Handling file system traversal and pattern matching using Python modules.
2. Building a clean command-line interface using argparse.
3. Automating file operations safely with shutil.


## Future Enhancements (Optional)

1. Add logging functionality to track files moved.
2. Implement dry-run mode to preview actions.
3. Add support for multiple file types or bulk extension filters.
4. Develop a cross-platform GUI with tools like Tkinter or PyQt.
