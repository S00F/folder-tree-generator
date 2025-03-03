import os
from pathlib import Path
from dotenv import load_dotenv
import sys
import shutil

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

def clean_tree_line(line):
    # Remove common tree characters
    tree_chars = ['│', '├', '└', '─', '│', '├', '└', '│', '├', '└', '─', '┬', '┴', '┤', '├', '┼', '┘', '┌', '┐']
    cleaned_line = line
    for char in tree_chars:
        cleaned_line = cleaned_line.replace(char, '')
    return cleaned_line.strip()

def calculate_depth(line):
    # Count both spaces and tree characters for depth
    depth = 0
    for char in line:
        if char in [' ', '│', '├', '└']:
            depth += 1
        else:
            break
    return depth

def parse_tree_structure(structure_file):
    with open(structure_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    structure = {}
    path_stack = [(0, structure)]  # (depth, dict) pairs
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        
        # Calculate actual depth and clean the line
        current_depth = calculate_depth(line)
        name = clean_tree_line(line)
        
        if not name:
            continue
        
        # Determine if it's a folder
        is_folder = name.endswith('/')
        if is_folder:
            name = name[:-1]
        
        # Find the appropriate parent based on depth
        while len(path_stack) > 1 and path_stack[-1][0] >= current_depth:
            path_stack.pop()
        
        # Ensure we have a valid parent
        if not path_stack:
            path_stack.append((0, structure))
            
        current_dict = path_stack[-1][1]
        
        # Add the new item
        if is_folder:
            current_dict[name] = {}
            path_stack.append((current_depth, current_dict[name]))
        else:
            current_dict[name] = None
    
    return structure

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = Path(base_path) / name
        
        if content is None:
            # Create file
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        else:
            # Create directory
            path.mkdir(parents=True, exist_ok=True)
            create_structure(path, content)

def clean_existing_structure(output_dir):
    path = Path(output_dir)
    if path.exists():
        try:
            shutil.rmtree(path)
            print(f"Existing structure at {output_dir} has been removed.")
        except Exception as e:
            print(f"Error while removing existing structure: {e}")
            sys.exit(1)

def main():
    # Load environment variables
    load_dotenv()
    
    # Get output directory from .env
    output_dir = os.getenv('OUTPUT_DIR')
    if not output_dir:
        raise ValueError("OUTPUT_DIR not found in .env file")
    
    # Clean existing structure if it exists
    clean_existing_structure(output_dir)
    
    # Read and parse tree structure
    structure = parse_tree_structure('tree_structure.txt')
    
    # Create the directory structure
    create_structure(output_dir, structure)
    print(f"Directory structure created successfully in {output_dir}")

if __name__ == "__main__":
    main()