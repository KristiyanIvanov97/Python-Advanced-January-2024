from functools import reduce


def operate(operator, *args):
    if operator == "+":
        return reduce(lambda x, y: x + y, args)
    elif operator == "-":
        return reduce(lambda x, y: x - y, args)
    elif operator == "/":
        if 0 in args:
            return
        return reduce(lambda x, y: x / y, args)
    elif operator == "*":
        return reduce(lambda x, y: x * y, args)


print(operate("+", 1, 2, 3))


# solution 2
#
# def operate(operator, *args):
#     if 0 in args and operator == "-":
#         return
#     return reduce(lambda x,y: eval(f"{x}{operator}{y}"), args)