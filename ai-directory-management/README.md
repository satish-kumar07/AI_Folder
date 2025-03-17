# AI Directory Management System

## Overview
The AI Directory Management System is designed to efficiently categorize and organize files using artificial intelligence. The system analyzes file content and metadata to predict appropriate categories, streamlining file management tasks.

## Project Structure
```
ai-directory-management
├── src
│   ├── main.py                # Entry point of the application
│   ├── ai
│   │   ├── model.py           # AI model for predicting file categories
│   │   └── train.py           # Functions for training the AI model
│   ├── utils
│   │   ├── file_operations.py  # Utility functions for file operations
│   │   └── logging_config.py   # Logging configuration
│   ├── config
│   │   └── settings.py        # Configuration settings for the application
│   └── tests
│       ├── test_model.py      # Unit tests for the AI model
│       └── test_file_operations.py # Unit tests for file operations
├── requirements.txt            # Project dependencies
├── .gitignore                  # Files and directories to ignore in version control
└── README.md                   # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd ai-directory-management
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Configure the application settings in `src/config/settings.py` to specify the source and target directories.

## Usage
To run the application, execute the following command:
```sh
python src/main.py <source_directory> <target_directory>
```
Replace `<source_directory>` and `<target_directory>` with the actual paths.

## Features
- **AI-based File Categorization**: Uses content and metadata analysis to categorize files into predefined categories.
- **Efficient File Organization**: Automatically organizes files into folders based on their categories.
- **Logging**: Logs file operations for tracking and debugging purposes.
- **Visualization**: Provides a visual representation of the file distribution by category.

## Visualization
The application includes a feature to visualize the distribution of files by category using a pie chart. This helps in understanding the organization of files at a glance.

## Example
Here is an example of how to use the application:
1. Prepare your source directory with various files.
2. Run the application:
   ```sh
   python src/main.py /path/to/source /path/to/target
   ```
3. The files will be organized into the target directory, and a pie chart will be displayed showing the distribution of files by category.

## Import Libraries
The following libraries are used in this project:
- **os**: For interacting with the operating system, such as file and directory operations.
- **sys**: For accessing command-line arguments.
- **joblib**: For loading and saving the AI model.
- **shutil**: For high-level file operations, such as copying and moving files.
- **matplotlib**: For creating visualizations, such as pie charts.
- **logging**: For logging file operations and debugging information.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.