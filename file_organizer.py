import os
import shutil

# 👉 Set the path to your 'sample' folder
base_folder = r"C:\Users\navee\Desktop\Sample"  # <-- Change this to your actual path

# Define file type mappings
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.webp', '.gif'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'code': ['.py', '.cpp', '.js', '.html', '.css'],
    'archives': ['.zip', '.rar', '.7z'],
    'music': ['.mp3', '.wav']
}

def move_file_to_folder(file_name, extension):
    moved = False
    for folder_name, extensions in file_types.items():
        if extension.lower() in extensions:
            destination = os.path.join(base_folder, folder_name)
            shutil.move(os.path.join(base_folder, file_name), destination)
            print(f"Moved {file_name} ➡️ {folder_name}")
            moved = True
            break
    if not moved:
        # Move to 'others' if no match
        destination = os.path.join(base_folder, 'others')
        shutil.move(os.path.join(base_folder, file_name), destination)
        print(f"Moved {file_name} ➡️ others")

# Go through each item in the sample folder
for item in os.listdir(base_folder):
    item_path = os.path.join(base_folder, item)
    if os.path.isfile(item_path):
        _, extension = os.path.splitext(item)
        move_file_to_folder(item, extension)

print("\n✅ All files moved to respective folders.")
