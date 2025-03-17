import os
import shutil
import logging
import mimetypes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def move_file(source_path, target_path):
    """Move a file from source to target path."""
    try:
        shutil.move(source_path, target_path)
        logging.info(f"Moved file from {source_path} to {target_path}")
    except Exception as e:
        logging.error(f"Error moving file from {source_path} to {target_path}: {e}")

def copy_file(source_path, target_path):
    """Copy a file from source to target path."""
    try:
        shutil.copy2(source_path, target_path)
        logging.info(f"Copied file from {source_path} to {target_path}")
    except Exception as e:
        logging.error(f"Error copying file from {source_path} to {target_path}: {e}")

def delete_file(file_path):
    """Delete a file at the specified path."""
    try:
        os.remove(file_path)
        logging.info(f"Deleted file at {file_path}")
    except Exception as e:
        logging.error(f"Error deleting file at {file_path}: {e}")

def categorize_file(file_name, categories):
    """Categorize a file based on its extension."""
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    for category, extensions in categories.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(source_dir, target_dir, model):
    """Organize files in the source directory using the provided model."""
    if not os.path.exists(source_dir):
        logging.error(f"Source directory {source_dir} does not exist.")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isfile(file_path):
            file_metadata = {
                'name': file_name,
                'size': os.path.getsize(file_path),
                'type': mimetypes.guess_type(file_path)[0] or 'application/octet-stream'
            }
            category = model.predict_category(file_metadata)
            target_folder = os.path.join(target_dir, category)
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            move_file(file_path, os.path.join(target_folder, file_name))
    logging.info("File organization completed.")