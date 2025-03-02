import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the tree structure from an external file
TREE_FILE = "tree_structure.txt"

# Get the output directory from the environment variable, default to 'generated_structure' if not set
output_directory = os.getenv("OUTPUT_DIRECTORY", "generated_structure")

def read_tree_structure(file_path):
    """Read tree structure from a file."""
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found. Please create the file with a valid tree structure.")
        exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def create_structure(base_path, structure):
    """Create files and folders based on the tree structure."""
    for line in structure.split("\n"):
        line = line.strip()
        if not line or line.startswith("├") or line.startswith("└"):
            continue
        
        clean_name = line.replace("│", "").replace("├", "").replace("└", "").strip()
        
        if clean_name.endswith("/"):  # It's a folder
            path = os.path.join(base_path, clean_name)
            os.makedirs(path, exist_ok=True)
        else:  # It's a file
            path = os.path.join(base_path, clean_name)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write(f"Content of {clean_name}")  # Default content

# Main execution
if __name__ == "__main__":
    # Create the base directory based on the environment variable
    os.makedirs(output_directory, exist_ok=True)

    # Read structure from external file
    tree_structure = read_tree_structure(TREE_FILE)

    # Create folders and files
    create_structure(output_directory, tree_structure)

    print(f"File and folder structure created in '{output_directory}'")
