rows = int(input())

matrix = [[int(x) for x in input().split(", ")] for x in range(rows)]

flatten_matrix = [num for row in matrix for num in row]

print(flatten_matrix)
