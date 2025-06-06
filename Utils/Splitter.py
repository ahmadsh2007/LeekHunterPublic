import os
import shutil
import re
import random

def split_folder_into_parts(input_folder, output_folder, n_parts,
                            accepted_extensions=None,
                            move_files=False,
                            shuffle=True,
                            filename_regex=None):
    """
    Splits files from input_folder into n_parts folders inside output_folder.

    Parameters:
    - input_folder: path to folder with files
    - output_folder: base output directory
    - n_parts: number of parts to split into
    - accepted_extensions: list of allowed extensions like ['.jpg', '.png'] or None for all
    - move_files: True to move files instead of copying
    - shuffle: True to randomly shuffle the files before splitting
    - filename_regex: optional regex string to filter filenames (e.g. '^img_.*')
    """

    # Create part folders
    for i in range(n_parts):
        os.makedirs(os.path.join(output_folder, f'part_{i+1}'), exist_ok=True)

    # List and filter files
    files = os.listdir(input_folder)

    if accepted_extensions:
        files = [f for f in files if os.path.splitext(f)[1].lower() in accepted_extensions]

    if filename_regex:
        pattern = re.compile(filename_regex)
        files = [f for f in files if pattern.match(f)]

    if shuffle:
        random.shuffle(files)

    # Split files into n_parts
    parts = [[] for _ in range(n_parts)]
    for idx, file in enumerate(files):
        parts[idx % n_parts].append(file)

    # Copy/move files
    for i, part_files in enumerate(parts):
        dest_folder = os.path.join(output_folder, f'part_{i+1}')
        for file in part_files:
            src = os.path.join(input_folder, file)
            dst = os.path.join(dest_folder, file)
            if move_files:
                shutil.move(src, dst)
            else:
                shutil.copy2(src, dst)

    print(f"✅ Done! {len(files)} files split into {n_parts} parts in '{output_folder}'.")

# ========================
# ✅ Example Usage Below
# ========================
if __name__ == "__main__":
    input_folder = r'C:\Your\Input\Path'
    output_folder = r'C:\Your\Output\Path'
    num_parts = 4

    split_folder_into_parts(
        input_folder=input_folder,
        output_folder=output_folder,
        n_parts=num_parts,
        accepted_extensions=['.jpg', '.jpeg', '.png'],  # None for all files
        move_files=False,       # True = move, False = copy
        shuffle=True,           # Shuffle files before splitting
        filename_regex=None     # e.g., r'^photo_\d+\.jpg$'
    )
