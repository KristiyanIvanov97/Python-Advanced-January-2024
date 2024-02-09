import os

filename = "my_first_file.txt"
path = os.path.join("resources", filename)

with open(path, "a") as file:
    file.write("I just created my first file!")
