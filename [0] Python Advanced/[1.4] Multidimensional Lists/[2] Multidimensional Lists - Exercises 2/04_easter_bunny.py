field_size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_eggs_collected = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(field_size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, pos in directions.items():
    row, col = [
        bunny_pos[0] + pos[0],
        bunny_pos[1] + pos[1]
    ]

    path = []
    eggs_collected = 0

    while 0 <= row < field_size and 0 <= col < field_size:
        if matrix[row][col] == 'X':
            break

        eggs_collected += int(matrix[row][col])
        path.append([row, col])

        row += pos[0]
        col += pos[1]

    if eggs_collected >= max_eggs_collected:
        max_eggs_collected = eggs_collected
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep='\n')
print(max_eggs_collected)
