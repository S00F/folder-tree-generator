# Folder Tree Generator

A simple Python script that generates files and folders from a tree structure stored in an external file.

## 📝 Project Overview

This project allows you to define a folder and file structure in a text file. The Python script reads the file and creates the corresponding directory and file structure in the system.

## 📌 How to Use

### 1. Clone the Repository
First, clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/folder-tree-generator.git
cd folder-tree-generator/src
```
2. Install Python
Make sure Python 3.x is installed on your system. You can check if its installed by running the following command in your terminal:

python3 --version  # For Mac/Linux
# or
python --version   # For Windows


3. Modify the tree_structure.txt (Optional)
Open the tree_structure.txt file and modify the directory structure according to your needs. This file defines the folder and file hierarchy.

Example structure:


root/
├── folder1/
│   ├── file1.txt
│   ├── file2.txt
│   └── subfolder1/
│       ├── file3.txt
│       └── file4.txt
├── folder2/
│   ├── file5.txt
│   └── subfolder2/
│       ├── file6.txt
└── file7.txt
4. Run the Script
Run the script to generate the directory structure. Depending on your system:

Windows:


python create_structure.py
Mac/Linux:


python3 create_structure.py
5. Check the Generated Structure
The folders and files will be created inside a folder called generated_structure. You can check the result there!