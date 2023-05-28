from collections import deque

clothes = deque([int(x) for x in input().split()])
shelf_space = int(input())

shelf_count = 1
current_shelf_space = shelf_space

while clothes:
    clothing = clothes.pop()

    if current_shelf_space >= clothing:
        current_shelf_space -= clothing
    else:
        shelf_count += 1
        current_shelf_space = shelf_space - clothing

print(shelf_count)
