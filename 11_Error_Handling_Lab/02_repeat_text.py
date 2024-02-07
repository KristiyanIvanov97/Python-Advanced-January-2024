text = input()

try:
    repeat = int(input())
    print(text * repeat)
except ValueError:
    print("Variable times must be an integer")
