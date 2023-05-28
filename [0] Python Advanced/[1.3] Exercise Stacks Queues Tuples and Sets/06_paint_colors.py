from collections import deque

words = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

result = []

while words:
    first_color = words.popleft()
    second_color = words.pop() if words else ""

    for color in (first_color + second_color, second_color + first_color):
        if color in all_colors:
            result.append(color)
            break
    else:
        for el in (first_color[:-1], second_color[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(secondary.keys()).intersection(result):
    if not secondary[color].issubset(result):
        result.remove(color)

print(result)
