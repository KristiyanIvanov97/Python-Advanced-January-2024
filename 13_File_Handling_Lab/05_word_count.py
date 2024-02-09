import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input.txt")
output_path = os.path.join("resources", "output.txt")

with open(words_path) as f:
    searched_words_as_text = f.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]

with open(text_path) as file:
    text_file = file.read().lower()

words_count = {}

for word in searched_words:
    pattern = re.compile(rf"\b{word}\b")
    result = re.findall(pattern, text_file)
    words_count[word] = len(result)

sorted_words = sorted(words_count.items(), key=lambda x: -x[1])

with open(output_path, "a") as output_file:
    for word, count in sorted_words:
        output_file.write(f"{word} - {count}\n")

