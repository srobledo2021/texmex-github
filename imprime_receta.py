import os

# File name
file_name = "recetas.md"

# exists?
if os.path.exists(file_name):
    # open file and read it
    with open(file_name, "r") as file_read:
        # keep content
        content = file_read.read()
        print(content)
else:
    print("File not found")

