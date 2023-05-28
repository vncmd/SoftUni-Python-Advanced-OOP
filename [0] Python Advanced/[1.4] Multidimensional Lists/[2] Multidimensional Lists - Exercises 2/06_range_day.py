def move(direction, steps):  # r = row; c = column
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < FIELD_SIZE and 0 <= c < FIELD_SIZE):
        return my_position
    if field[r][c] == 'x':
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < FIELD_SIZE and 0 <= c < FIELD_SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


FIELD_SIZE = 5
field = []

targets = 0
hit_targets = 0
hit_target_pos = []

my_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(FIELD_SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]

    targets += field[row].count('x')

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == 'move':
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == 'shoot':
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            hit_target_pos.append(target_down_pos)
            hit_targets += 1

        if hit_targets == targets:
            print(f'Training completed! All {targets} targets hit.')
            break

if hit_targets < targets:
    print(f'Training not completed! {targets - hit_targets} targets left.')

print(*hit_target_pos, sep="\n")
