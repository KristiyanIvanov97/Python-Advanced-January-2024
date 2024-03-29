from collections import deque

stack = deque()

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        number = int(command[1])
        stack.append(number)
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))

stack.reverse()

print(*stack, sep=", ")

