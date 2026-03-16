import shutil
import os

# Create a backup copy of a file
source = "data.txt"
destination = "data_backup.txt"

if os.path.exists(source):
    shutil.copy(source, destination)
    print(f"Successfully copied {source} to {destination}")

# Clean up: delete the backup file
if os.path.exists(destination):
    os.remove(destination)
    print(f"Temporary file {destination} removed.")