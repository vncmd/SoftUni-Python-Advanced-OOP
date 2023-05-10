stack_parentheses = []

data = input()

for idx in range(len(data)):
    if data[idx] == "(":
        stack_parentheses.append(idx)

    elif data[idx] == ")":
        start_position = stack_parentheses.pop()
        end_position = idx + 1
        print(data[start_position:end_position])
