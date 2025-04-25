"""
GUI-based file compression tool using FreeSimpleGUI.

This script allows users to select multiple files and a destination folder,
and then compress those files into a ZIP archive using the make_archive
function from the zip_creator module.
"""

import FreeSimpleGUI as sg
from zip_creator import make_archive

# Creates a text label widget that instructs the user to select files to compress.
label1 = sg.Text("Select files to compress:")
# Creates an input field where selected file paths will appear.
input1 = sg.Input()
#sg.FilesBrowse allow the user to select files on their file system.
choose_button1 = sg.FilesBrowse("Choose", key="files")

# Creates a second label to prompt the user to 
# choose where the compressed zip file will be saved.
label2 = sg.Text("Select destination folder:")
# Creates another input field to display the selected folder path.
input2 = sg.Input()
#sg.FolderBrowse allow the user to select folders on their file system.
choose_button2 = sg.FolderBrowse("Choose", key="folder")

# Adds a button labeled "Compress" that will trigger the compression action when clicked.
compress_button = sg.Button("Compress")
# Creates a text element (initially empty) that 
# will later be used to show a success message after compression.
output_label = sg.Text(key="output", text_color="green")

# Creates the GUI window titled "File Zipper".
# The layout defines three rows:
# Row 1: file label, input field, and file browse button
# Row 2: folder label, input field, and folder browse button
# Row 3: compress button and output label
window = sg.Window("File Zipper", 
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2], 
                           [compress_button, output_label]])

while True:
    # Waits for a user action (event), 
    # such as clicking a button or selecting files/folders.
    # event contains the name of the event (e.g. button clicked), 
    # and values is a dictionary of inputs.
    event, values = window.read()
    # If the user closes the window (clicks X), exit the loop
    if event == sg.WIN_CLOSED:
        break
    print(event, values)
    # Gets the file paths selected by the user (under key "files"), 
    # and splits them into a list (separated by semicolons ;, 
    # which is how the GUI gives multiple file paths).
    filepaths = values["files"].split(";")
    # Gets the selected destination folder path from the GUI (under key "folder").
    folder = values["folder"]
    # Calls your custom make_archive() function to compress 
    # the selected files into the chosen folder.
    make_archive(filepaths, folder)
    # Updates the output_label text to show a success message in the GUI.
    window["output"].update(value="Compression completed!")

# Closes the GUI window when the loop ends.
window.close()

