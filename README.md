# PyLS

A simple Python command-line application that mimics the basic functionality of the Unix `ls` command.

## Features

- 📂 List files and directories
- 📄 Display detailed information using the `-l` option
- 📦 Show file size in MB
- 🕒 Display last modification time
- 🐍 Built with Python standard library only
- ⚡ Uses `argparse`, `pathlib`, and `datetime`

## Requirements

- Python 3.10+

## Usage

List directory contents:

```bash
python script.py .
```

List files with additional details:

```bash
python script.py . -l
```

You can also specify any directory:

```bash
python script.py "C:\Users\Username\Downloads"
```

## Example Output

Normal mode:

```
file1.txt
photo.png
documents
```

Long mode:

```
0.24 MB 14:32 file1.txt
3.17 MB 09:11 photo.png
0.00 MB 18:42 documents
```

## Technologies

- Python
- argparse
- pathlib
- datetime

## Project Structure

```
.
├── script.py
└── README.md
```

## Learning Purpose

This project was built as a practice exercise for learning:

- Command Line Interfaces (CLI)
- Argument parsing with argparse
- File system operations
- Working with pathlib
- Python standard library

