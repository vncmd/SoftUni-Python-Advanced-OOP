def check_capture(attacker, defender):
    row_att = attacker[0]
    col_att = attacker[1]
    row_def = defender[0]
    col_def = defender[1]

    if row_att - 1 >= 0 and col_att - 1 >= 0:
        if row_att - 1 == row_def and col_att - 1 == col_def:

            return [row_att - 1, col_att - 1]

    if row_att - 1 >= 0 and col_att + 1 < 8:
        if row_att - 1 == row_def and col_att + 1 == col_def:

            return [row_att - 1, col_att + 1]
    if row_att + 1 < 8 and col - 1 >= 0:
        if row_att + 1 == row_def and col_att - 1 == col_def:

            return [row_att + 1, col_att - 1]

    if row_att + 1 < 8 and col + 1 < 8:
        if row_att + 1 == row_def and col_att + 1 == col_def:

            return [row_att + 1, col_att + 1]


board = []
for _ in range(8):
    board.append(input().split())

white_coordinates = []
black_coordinates = []

pos_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}

pos_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(8):
    for col in range(8):
        if board[row][col] == "w":
            white_coordinates = [row, col]

        if board[row][col] == "b":
            black_coordinates = [row, col]

for _ in range(8):
    capture_on = check_capture(white_coordinates, black_coordinates)

    if capture_on:
        position = pos_col[capture_on[1]] + pos_row[capture_on[0]]

        print(f"Game over! White win, capture on {position}.")

        break

    white_coordinates[0] -= 1

    if white_coordinates[0] == 0:
        position = pos_col[white_coordinates[1]] + pos_row[white_coordinates[0]]

        print(f"Game over! White pawn is promoted to a queen at {position}.")

        break

    capture_on = check_capture(black_coordinates, white_coordinates)
    if capture_on:
        position = pos_col[capture_on[1]] + pos_row[capture_on[0]]

        print(f"Game over! Black win, capture on {position}.")

        break

    black_coordinates[0] += 1

    if black_coordinates[0] == 7:
        position = pos_col[black_coordinates[1]] + pos_row[black_coordinates[0]]

        print(f"Game over! Black pawn is promoted to a queen at {position}.")

        break

# Different solution:


# def save_pos(search_for, index_to_save, r):
#     if search_for in board[r]:
#         positions[index_to_save].append(r)
#         positions[index_to_save].append(board[r].index(search_for))
#
#
# SIZE = 8
#
# board = []
# positions = [[], []]
#
# for row in range(SIZE):
#     board.append(input().split())
#
#     save_pos("w", 0, row)
#     save_pos("b", 1, row)
#
# if abs(positions[0][1] - positions[1][1]) != 1 or positions[1][0] > positions[0][0]:
#
#     if SIZE - positions[0][0] - 1 <= positions[1][0]:
#         print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
#
#     else:
#         print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
#
# else:
#     place = (positions[0][0] + positions[1][0]) // 2
#
#     if positions[0][0] % 2 == positions[1][0] % 2:
#         print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
#
#     else:
#         print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")
