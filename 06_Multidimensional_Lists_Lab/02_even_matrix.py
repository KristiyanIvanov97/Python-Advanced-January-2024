rows = int(input())

matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0]for row in range(rows)]

print(matrix)




# solution with else condition and replace odd numbers with 0

# rows = int(input())
#
# matrix = [[int(x) if int(x) % 2 == 0 else 0 for x in input().split(", ")] for row in range(rows)]
#
# print(matrix)
