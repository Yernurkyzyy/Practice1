import os

# Get current working directory
current_path = os.getcwd()
print(f"Current Directory: {current_path}")

# Create a new directory safely
folder_name = "practice_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Directory '{folder_name}' created.")

# List all files and directories in current path
print("Contents of current directory:")
for item in os.listdir("."):
    print(f"- {item}")