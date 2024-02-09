import os
from string import punctuation

text_file_path = os.path.join("resources", "text_2.txt")
output_file_path = os.path.join("resources", "output_file_1.txt")

with open(text_file_path) as file:
    text = file.readlines()

with open(output_file_path, "a") as output_file:
    for row in range(len(text)):
        letters, marks = 0, 0

        for symbol in text[row]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f"Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n")
