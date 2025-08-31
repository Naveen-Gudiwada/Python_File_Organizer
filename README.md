# Python_File_Organizer

## 📂 Automated File Organizer using Python
### 📌 Project Overview

This project is a Python-based file organization tool that automatically sorts files in a given folder into categorized subfolders based on their file extensions. It helps maintain a clean and structured directory by moving files such as documents, images, videos, music, and code into respective folders.

### 🎯 Objectives

- Automate the process of organizing files.
- Categorize files into different folders based on their type.
- Improve productivity and save time by reducing manual file management.

### 🛠️ Technologies Used

- Python (3.x)
- os module – for interacting with the file system.
- shutil module – for moving files between folders.

📁 Folder Structure (After Execution)

```markdown
Sample/
│── images/
│── videos/
│── documents/
│── code/
│── archives/
│── music/
│── others/

```

### 📜 How It Works

1. Define the base folder (Sample directory in this case).
2. Create a dictionary (file_types) that maps file extensions to categories.
3. For each file in the folder:
    - Check its extension.
    - Move it to the corresponding folder.
    - If no match is found, move it to the others folder.
4. Print a log of all moved files.

### 💻 Code Explanation
### Import Libraries
```python
import os
import shutil
```
- os → to list files, check paths, and handle extensions.
- shutil → to move files between folders.

### File Type Mapping
```python
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.webp', '.gif'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'code': ['.py', '.cpp', '.js', '.html', '.css'],
    'archives': ['.zip', '.rar', '.7z'],
    'music': ['.mp3', '.wav']
}
```
- Each key represents a folder.
- Each value is a list of file extensions belonging to that category.

### File Movement Function
```Python
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
        destination = os.path.join(base_folder, 'others')
        shutil.move(os.path.join(base_folder, file_name), destination)
        print(f"Moved {file_name} ➡️ others")
```
- Moves file to the correct folder.
- If extension is unknown, sends it to others.

### Execution Loop
```python
for item in os.listdir(base_folder):
    item_path = os.path.join(base_folder, item)
    if os.path.isfile(item_path):
        _, extension = os.path.splitext(item)
        move_file_to_folder(item, extension)
```
- Loops through all files in the folder.
- Extracts file extension and calls the move function.

### 🚀 How to Run
1. Copy the script into a Python file (file_organizer.py).
2. Change the base_folder path to your target directory.
3. Run the script:
```bash
python file_organizer.py
```
4. Watch your messy folder become clean and structured automatically ✅

### 📈 Future Improvements
- Add GUI for easier use (Tkinter / PyQt).
- Add option for user-defined categories.
- Implement logging into a file instead of console.
- Add undo functionality (restore files to original location).

### 🤝 Acknowledgments
- Developed using Python standard libraries (os, shutil).
- Inspired by the need to maintain a clutter-free desktop.
