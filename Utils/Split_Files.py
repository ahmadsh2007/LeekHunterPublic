import os
import shutil
import random
import re

def split_files(input_folder, output_folder_1, output_folder_2, 
                split_ratio=0.7, 
                accepted_extensions=None,
                move_files=False,
                filename_regex=None):
    """
    Splits files from input_folder into output_folder_1 and output_folder_2.

    Parameters:
    - input_folder: path to folder with files
    - output_folder_1: path for first split output
    - output_folder_2: path for second split output
    - split_ratio: float between 0 and 1
    - accepted_extensions: list of extensions like ['.jpg', '.txt'] (lowercase, with dot)
    - move_files: if True, files are moved instead of copied
    - filename_regex: optional regex string to filter filenames (e.g. '^img_.*')
    """

    os.makedirs(output_folder_1, exist_ok=True)
    os.makedirs(output_folder_2, exist_ok=True)

    all_files = os.listdir(input_folder)

    # Apply extension filter
    if accepted_extensions:
        all_files = [f for f in all_files if os.path.splitext(f)[1].lower() in accepted_extensions]

    # Apply regex filter
    if filename_regex:
        pattern = re.compile(filename_regex)
        all_files = [f for f in all_files if pattern.match(f)]

    random.shuffle(all_files)

    num_files_1 = int(len(all_files) * split_ratio)
    num_files_2 = len(all_files) - num_files_1

    for i, file in enumerate(all_files):
        source_path = os.path.join(input_folder, file)
        if i < num_files_1:
            destination_path = os.path.join(output_folder_1, file)
        else:
            destination_path = os.path.join(output_folder_2, file)

        if move_files:
            shutil.move(source_path, destination_path)
        else:
            shutil.copy2(source_path, destination_path)

    print(f"✅ Split complete: {num_files_1} files in '{output_folder_1}', {num_files_2} files in '{output_folder_2}'.")

# ========================
# ✅ Example Usage Below
# ========================
if __name__ == "__main__":
    input_folder_path = r'C:\Your\Input\Path'
    output_folder_1_path = r'C:\Your\Output1\Path'
    output_folder_2_path = r'C:\Your\Output2\Path'

    split_files(
        input_folder=input_folder_path,
        output_folder_1=output_folder_1_path,
        output_folder_2=output_folder_2_path,
        split_ratio=0.75,
        accepted_extensions=['.png', '.jpg', '.jpeg', '.gif'],  # Set to None for all file types
        move_files=False,  # Set True to move instead of copy
        filename_regex=None  # Example: r'^img_.*' to match files starting with 'img_'
    )
