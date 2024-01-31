rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(col) for col in input().split(", ")]for row in range(rows)]
total_sum = 0
for row in matrix:
    total_sum += sum(row)

print(total_sum)
print(matrix)


# solution 2

# rows, cols = [int(x) for x in input().split(", ")]
#
# matrix = []
# total_amount = 0
#
# for row in range(rows):
#     row_data = [int(x) for x in input().split(", ")]
#     total_amount += sum(row_data)
#     matrix.append(row_data)
#
# print(total_amount)
# print(matrix)
