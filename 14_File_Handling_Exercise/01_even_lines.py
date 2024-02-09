import os

text_file_path = os.path.join("resources", "text_1.txt")
symbols = ("-", ",", ".", "!", "?")

with open(text_file_path) as f:
    text_file = f.readlines()

for row in range(0, len(text_file), 2):
    for symbol in symbols:
        text_file[row] = text_file[row].replace(symbol, "@")

    print(*text_file[row].split()[::-1])


