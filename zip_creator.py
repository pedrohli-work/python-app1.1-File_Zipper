"""
This module provides a utility function to compress multiple files into a ZIP archive.

The main function, `make_archive`, takes a list of file paths and a destination directory,
and creates a zip file named 'compressed.zip' containing the selected files.
"""

import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    """
    Compresses the given list of files into a zip archive named 'compressed.zip'.
    Args:
        filepaths (list): A list of file paths (as strings) to be included in the ZIP.
        dest_dir (str): The destination folder where the ZIP file will be created.
    Returns:
        None
    """
    # Creates a full path to the destination zip file by 
    # joining the dest_dir with the filename "compressed.zip" using pathlib.Path.
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    # Creating a zip file in write mode
    # Opens a new ZIP file in write mode ('w') at dest_path.
    with zipfile.ZipFile(dest_path, 'w') as archive:
        # Loops over each path in the list of file paths provided.
        for filepath in filepaths:
            # Converts each string filepath into a Path object
            filepath = pathlib.Path(filepath)
            # object has a write method which expects the file path.
            archive.write(filepath, arcname=filepath.name)


# if __name__ == "__main__":
# make_archive(filepaths=["bonus1.py", "bonus2.1.py"], dest_dir="dest")

