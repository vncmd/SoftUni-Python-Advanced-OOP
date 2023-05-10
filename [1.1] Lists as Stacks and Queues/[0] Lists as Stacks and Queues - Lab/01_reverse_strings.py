data = input()

text_stack = list(data)

while text_stack:
    removed_element = text_stack.pop()
    print(removed_element, end="")
