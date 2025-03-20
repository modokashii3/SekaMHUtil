import os

def find_empty_folders(root_folder):
    empty_folders = []
    for folder, subfolders, files in os.walk(root_folder, topdown=False):
        if not any((subfolders, files)):
            empty_folders.append(folder)
    return empty_folders

def delete_empty_folders(root_folder):
    empty_folders = find_empty_folders(root_folder)
    for folder in empty_folders:
        try:
            os.rmdir(folder)
            print(f"Deleted empty folder: {folder}")
        except OSError as e:
            print(f"Error deleting folder {folder}: {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    delete_empty_folders(current_directory)

input("Press Enter to exit...")
