import os
import shutil
from datetime import datetime


def organize_files(source_dir, target_dir=None):
    """
    Organize files from source directory into categorized folders
    """
    # If no target directory is specified, create one in the source directory
    if target_dir is None:
        target_dir = os.path.join(source_dir, "Organized_Files")

    # Create target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Define file categories and their extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Presentations": [".ppt", ".pptx"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Video": [".mp4", ".avi", ".mov", ".wmv", ".mkv", ".flv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"]
    }

    # Create category directories
    for category in categories:
        category_path = os.path.join(target_dir, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # Create "Other" directory for uncategorized files
    other_path = os.path.join(target_dir, "Other")
    if not os.path.exists(other_path):
        os.makedirs(other_path)

    # Track statistics
    stats = {
        "total_files": 0,
        "organized_files": 0,
        "categories": {}
    }

    # Initialize category counts
    for category in categories:
        stats["categories"][category] = 0
    stats["categories"]["Other"] = 0

    # Walk through source directory
    print(f"Scanning {source_dir} for files...")

    for root, _, files in os.walk(source_dir):
        for file in files:
            # Skip the script file itself
            if file == os.path.basename(__file__):
                continue

            # Skip files in the target directory
            if target_dir in root:
                continue

            file_path = os.path.join(root, file)
            stats["total_files"] += 1

            # Get file extension
            _, extension = os.path.splitext(file)
            extension = extension.lower()

            # Determine category
            category_found = False
            for category, extensions in categories.items():
                if extension in extensions:
                    destination = os.path.join(target_dir, category, file)
                    category_found = True
                    stats["categories"][category] += 1
                    break

            # If no category found, move to "Other"
            if not category_found:
                destination = os.path.join(target_dir, "Other", file)
                stats["categories"]["Other"] += 1

            # Handle duplicate filenames
            if os.path.exists(destination):
                name, ext = os.path.splitext(file)
                destination = os.path.join(os.path.dirname(destination),
                                           f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}")

            # Move the file
            try:
                shutil.move(file_path, destination)
                stats["organized_files"] += 1
                print(f"Moved: {file} -> {os.path.basename(os.path.dirname(destination))}")
            except Exception as e:
                print(f"Error moving {file}: {e}")

    # Print summary
    print("\nOrganization Complete!")
    print(f"Total files found: {stats['total_files']}")
    print(f"Files organized: {stats['organized_files']}")
    print("\nFiles by category:")

    for category, count in stats["categories"].items():
        if count > 0:
            print(f"  {category}: {count}")

    return stats


if __name__ == "__main__":
    # Get user input for source directory
    source_directory = input("Enter the directory path to organize (press Enter for current directory): ")

    # Use current directory if none specified
    if not source_directory:
        source_directory = os.getcwd()

    # Organize files
    if os.path.exists(source_directory):
        organize_files(source_directory)
    else:
        print(f"Directory not found: {source_directory}")
