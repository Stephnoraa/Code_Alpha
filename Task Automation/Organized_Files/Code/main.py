import os
import shutil

# Define the directory to organize
DOWNLOADS_FOLDER = r"C:\Users\!ADMIN!\Downloads"  # Change this path accordingly

# Define file categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"]
}


def organize_files():
    for file in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, file)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()

            for category, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    category_path = os.path.join(DOWNLOADS_FOLDER, category)

                    if not os.path.exists(category_path):
                        os.makedirs(category_path)  # Create folder if not exists

                    shutil.move(file_path, os.path.join(category_path, file))
                    print(f"Moved {file} to {category}")


if __name__ == "__main__":
    organize_files()