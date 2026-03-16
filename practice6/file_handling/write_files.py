with open("data.txt", "w") as f:
    f.write("Hello Python!\n")
    f.write("This is a file handling practice.\n")

# Appending new content
with open("data.txt", "a") as f:
    f.write("Adding a new line to the file.\n")

print("File 'data.txt' has been created and updated.")