import shutil
import os

# 1. Setup: Create a dummy file to work with
filename = "original.txt"
with open(filename, "w") as f:
    f.write("This is the original content.")

print(f"File '{filename}' created.")

# 2. Copying a file
# shutil.copy(source, destination)
backup_file = "backup_copy.txt"
shutil.copy(filename, backup_file)
print(f"File copied successfully to '{backup_file}'.")

# 3. Moving a file
# First, create a folder to move the file into
folder_name = "archive"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Move the file into the new folder
moved_location = os.path.join(folder_name, "moved_original.txt")
shutil.move(filename, moved_location)
print(f"Original file moved to '{moved_location}'.")

# 4. Deleting files safely
# Check if file exists before deleting to avoid errors
if os.path.exists(backup_file):
    os.remove(backup_file)
    print(f"File '{backup_file}' has been deleted.")
else:
    print(f"The file '{backup_file}' does not exist.")

# 5. Summary of Directory Content
print("\nFinal directory contents:")
print(os.listdir("."))