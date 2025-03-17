# ai-directory-management/ai-directory-management/src/main.py

import os
import sys
from ai.model import FileCategorizer
from utils.file_operations import organize_files

def main():
    # Initialize the AI model for file categorization
    model = FileCategorizer()
    
    # Load the model if necessary
    model.load_model()

    # Organize files in the specified source directory
    organize_files(SOURCE_DIR, TARGET_DIR, model)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <source_directory> <target_directory>")
        sys.exit(1)

    # Update source and target directories from command line arguments
    SOURCE_DIR = sys.argv[1]
    TARGET_DIR = sys.argv[2]

    main()