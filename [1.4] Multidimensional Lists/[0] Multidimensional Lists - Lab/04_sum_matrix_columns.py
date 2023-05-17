rows, cols = [int(el) for el in input().split(", ")]

matrix = []
for _ in range(rows):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

for col_idx in range(cols):
    col_sum = 0
    for row_idx in range(rows):
        col_sum += matrix[row_idx][col_idx]

    print(col_sum)
