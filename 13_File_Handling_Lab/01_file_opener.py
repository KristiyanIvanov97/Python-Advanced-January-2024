import os
file = "text.txt"
path = os.path.join("resources", file)

try:
    file = open(path, "r")
    print("File found")
except FileNotFoundError:
    print("File is not found")
