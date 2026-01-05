import os
import shutil

# Put EXACT path of your Downloads folder
path =  r"C:\Users\Nikhil\OneDrive\Desktop\Downloads"


file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3", ".wav"]
}

# Create folders
for folder in file_types:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)


# Move files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path, folder, file))
                break
print("Files organized successfully.")
