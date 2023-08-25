import os

def rename_files_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith("l_english.yml"):
                old_path = os.path.join(root, filename)
                new_filename = filename.replace("l_english.yml", "l_german.yml")
                new_path = os.path.join(root, new_filename)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    target_directory = input("Enter the target directory path: ")
    rename_files_in_directory(target_directory)
