rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]

biggest_square = []
biggest_sum = float("-inf")

for row in range(rows - 1):
    for col in range(cols - 1):
        curr_value = matrix[row][col]
        right_value = matrix[row][col + 1]
        bottom_right_value = matrix[row + 1][col + 1]
        bottom_value = matrix[row + 1][col]

        total_sum = curr_value + right_value + bottom_right_value + bottom_value
        if total_sum > biggest_sum:
            biggest_sum = total_sum
            biggest_square = [[curr_value, right_value], [bottom_value, bottom_right_value]]

print(*biggest_square[0])
print(*biggest_square[1])
print(biggest_sum)
