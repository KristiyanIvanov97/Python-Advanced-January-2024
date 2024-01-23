expression = input()

start_par = []
for i in range(len(expression)):
    if expression[i] == "(":
        start_par.append(i)

    elif expression[i] == ")":
        start_index = start_par.pop()
        end_index = i + 1
        print(expression[start_index:end_index])

