import os

filename = "numbers.txt"
path = os.path.join("resources", filename)

with open(path, "r") as file:
    lines = file.readlines()
    print(sum(int(num) for num in lines))
    # for line in lines:
    #     print(line[:-1], end=" ")
