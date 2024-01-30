from collections import deque

expression = deque(input().split())  # [1, 2 + 4 ]
index = 0

while len(expression) > 1:
    element = expression[index]

    if element == "*":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "+":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) // int(expression.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))

    if element in "*+/-":
        del expression[1]
        index = 1

    index += 1

print(expression[0])
