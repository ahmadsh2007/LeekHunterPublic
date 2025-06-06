import os
import shutil
from tqdm import tqdm

# Source folders
folders = [
    r'Folder 1',
    r'Folder 2',
    r'Folder 3',
    r'Folder n',
]

# Destination folder
destination_folder = r'Destination Folder'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Gather all files first
all_files = []
for folder in folders:
    if not folder:
        continue
    for filename in os.listdir(folder):
        all_files.append((folder, filename))

conflicts = []

# Use tqdm to show a progress bar
for folder, filename in tqdm(all_files, desc="Merging images", unit="file"):
    src_path = os.path.join(folder, filename)
    dest_path = os.path.join(destination_folder, filename)

    # If file already exists, rename slightly to avoid overwriting
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while True:
            new_filename = f"{base}_{counter}{ext}"
            dest_path = os.path.join(destination_folder, new_filename)
            if not os.path.exists(dest_path):
                conflicts.append((filename, new_filename))  # Record conflict
                break
            counter += 1

    shutil.copy(src_path, dest_path)

# Done
print("\nImages merged successfully.")
if conflicts:
    print("\nConflicts detected and resolved:")
    for original, renamed in conflicts:
        print(f" - {original} -> {renamed}")
else:
    print("\nNo conflicts detected.")