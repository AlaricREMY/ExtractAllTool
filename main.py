from zipfile import ZipFile
import os

# This program extracts every zip file present in the CURRENT WORKING FOLDER (Aka the folder you currently execute the program from). 
# If you want to edit this, edit the current_path variable.

folder = ""
# Leave empty if you want the files to be extracted to the folder they are currently in, or replace by the path to the folder you want to use.
# Use %CURRENT_PATH% if you want to use a folder inside the one that currently hosts the program.

current_path = os.getcwd()  # Uses the current working directory
files_list = os.listdir(current_path)

path_to_extract_to = path_to_extract_to = folder.replace("%CURRENT_PATH%", current_path).replace("/", "\\")

current_path_display = current_path.replace("//", "\\")
path_to_extract_to_display = path_to_extract_to.replace("//", "\\")

print(f"- ExtractAll Tool -\n  By EnderTower\n\nExtracting files in folder '{current_path_display}'\nTo folder '{path_to_extract_to_display}'\n")

for file in files_list:
    if file.endswith(".zip"):
        with ZipFile(file) as zip:
            zip.extractall(path_to_extract_to)
        print(f"Successfully extracted file '{file}'..")
    else:
        continue

print("\nAll the files were successfully extracted.")
