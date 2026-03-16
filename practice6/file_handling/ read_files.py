# Reading from a file using different methods

print("--- Reading whole file ---")
with open("data.txt", "r") as f:
    print(f.read())

print("--- Reading line by line ---")
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip()) 