rows, cols = [int(x) for x in input().split()]

matrix = []
start_index = 97
for row in range(start_index, start_index + rows):
    for col in range(row, row + cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()
