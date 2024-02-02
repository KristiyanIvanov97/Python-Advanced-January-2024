rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]
maximum_sum = float("-inf")
sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if total_sum > maximum_sum:
            maximum_sum = total_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {maximum_sum}")
[print(*matrix)for matrix in sub_matrix]




















# solution 2
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[int(x) for x in input().split()] for row in range(rows)]
# maximum_sum = float("-inf")
# sub_matrix = []
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         first_row = matrix[row][col:col + 3]
#         curr_value = matrix[row][col]
#         down_value = matrix[row + 1][col]
#         double_down_value = matrix[row + 2][col]
#         diagonal_value = matrix[row + 1][col + 1]
#         double_diagonal_value = matrix[row + 2][col + 2]
#         two_down_right_value = matrix[row + 2][col + 1]
#         right_value = matrix[row][col + 1]
#         double_right_value = matrix[row][col + 2]
#         two_right_down_value = matrix[row + 1][col + 2]
#
#         total_sum = curr_value + down_value + double_down_value + \
#                     diagonal_value + double_diagonal_value + two_down_right_value + \
#                     right_value + double_right_value + two_right_down_value
#
#         if total_sum > maximum_sum:
#             maximum_sum = total_sum
#             sub_matrix = [[curr_value, right_value, double_right_value],
#                           [down_value, diagonal_value, two_right_down_value],
#                           [double_down_value, two_down_right_value, double_diagonal_value]]
#
# print(f"Sum = {maximum_sum}")
# print(" ".join(str(value) for value in sub_matrix[0]))
# print(" ".join(str(value) for value in sub_matrix[1]))
# print(" ".join(str(value) for value in sub_matrix[2]))
