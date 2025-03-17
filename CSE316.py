import os
import shutil
import logging
import hashlib
from datetime import datetime
import sys

# Configure logging
logging.basicConfig(filename='file_management.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Default categorization rules based on file extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []  # Default for uncategorized files
}

class DirectoryManager:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.duplicates_dir = os.path.join(target_dir, "Duplicates")
        self.categories = CATEGORIES

    def create_category_folders(self):
        """Create category folders in the target directory if they don't exist."""
        os.makedirs(self.target_dir, exist_ok=True)
        os.makedirs(self.duplicates_dir, exist_ok=True)
        for category in self.categories.keys():
            folder_path = os.path.join(self.target_dir, category)
            os.makedirs(folder_path, exist_ok=True)

    def get_file_hash(self, file_path):
        """Generate a hash for a file to detect duplicates."""
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    def categorize_file(self, file_name):
        """Determine the category of a file based on its extension."""
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()
        for category, extensions in self.categories.items():
            if ext in extensions:
                return category
        return "Others"

    def move_file(self, file_path, target_folder, file_name):
        """Move a file to its target folder and log the action."""
        target_path = os.path.join(target_folder, file_name)
        if os.path.exists(target_path):
            file_hash = self.get_file_hash(file_path)
            existing_hash = self.get_file_hash(target_path)
            if file_hash == existing_hash:
                logging.info(f"Duplicate found: {file_name}")
                shutil.move(file_path, os.path.join(self.duplicates_dir, file_name))
                return
            else:
                # Rename file if it's not a duplicate but has the same name
                base_name, ext = os.path.splitext(file_name)
                new_name = f"{base_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
                target_path = os.path.join(target_folder, new_name)
        
        shutil.move(file_path, target_path)
        logging.info(f"Moved {file_name} to {target_folder}")

    def organize_files(self):
        """Scan the source directory and organize files."""
        if not os.path.exists(self.source_dir):
            logging.error(f"Source directory {self.source_dir} does not exist.")
            return

        self.create_category_folders()

        for file_name in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, file_name)
            if os.path.isfile(file_path):
                category = self.categorize_file(file_name)
                target_folder = os.path.join(self.target_dir, category)
                self.move_file(file_path, target_folder, file_name)

        logging.info("File organization completed.")

    def add_custom_rule(self, category, extensions):
        """Add a custom category and its associated extensions."""
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].extend(extensions)
        logging.info(f"Added custom rule: {category} -> {extensions}")

# Example usage
if __name__ == "__main__":
    source_directory = "path/to/source/folder"  # Replace with your source folder
    target_directory = "path/to/target/folder"  # Replace with your target folder

    manager = DirectoryManager(source_directory, target_directory)

    # Optional: Add a custom rule
    manager.add_custom_rule("Presentations", [".ppt", ".pptx"])

    # Organize the files
    if len(sys.argv) != 3:
        print("Usage: python CSE316.py <source_directory> <target_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    manager = DirectoryManager(source_directory, target_directory)

    # Optional: Add a custom rule
    manager.add_custom_rule("Presentations", [".ppt", ".pptx"])

    # Organize the files
    manager.organize_files()