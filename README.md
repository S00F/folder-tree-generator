# Folder Tree Generator

A simple Python script that generates files and folders from a tree structure stored in an external file.

## 📝 Project Overview

This project allows you to define a folder and file structure in a text file. The Python script reads the file and creates the corresponding directory and file structure in the system. You can specify the output directory using an environment variable in a `.env` file.

## 📌 How to Use

### 1. Clone the Repository
First, clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/folder-tree-generator.git
cd folder-tree-generator/src
```
2. Install Python and Dependencies
Make sure Python 3.x is installed on your system. You can check if it's installed by running the following command in your terminal:

```sh
python3 --version  # For Mac/Linux
# or
python --version   # For Windows
```

If Python is not installed, you can download it from the official Python website.

Once Python is installed, install the required dependencies by running:

```sh
pip install -r requirements.txt
```
If requirements.txt does not exist, you can install the python-dotenv package directly:

```sh
pip install python-dotenv
```
3. Set the Output Directory in the .env File
Create a .env file in the root of your project and set the OUTPUT_DIRECTORY variable to specify where you want the folder and file structure to be generated.

Example .env file:

```env
OUTPUT_DIRECTORY=./generated_structure
```
You can change the value of OUTPUT_DIRECTORY to any path where you'd like the structure to be created.

4. Modify the tree_structure.txt (Optional)
Open the tree_structure.txt file and modify the directory structure according to your needs. This file defines the folder and file hierarchy.

Example structure:

```
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
```
5. Run the Script
Run the script to generate the directory structure. Depending on your system:

Windows:

```sh
python create_structure.py
```
Mac/Linux:

```sh
python3 create_structure.py
```
6. Check the Generated Structure
The folders and files will be created inside the directory specified in the .env file under the OUTPUT_DIRECTORY variable. If no .env file is found, it defaults to generated_structure.

📂 Project Structure
```bash
folder-tree-generator/
├── src/
│   ├── create_structure.py  # Main Python script that creates the structure
│   ├── tree_structure.txt   # External file that defines the tree structure
│   ├── .env                 # Environment variables (OUTPUT_DIRECTORY)
├── README.md                # This documentation file
├── .gitignore               # Git ignore file for unnecessary files
└── requirements.txt         # Dependencies file (python-dotenv)

