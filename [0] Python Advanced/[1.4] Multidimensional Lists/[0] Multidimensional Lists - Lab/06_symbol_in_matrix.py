def find_element(matrix_, element):
    for row_idx in range(rows):
        for col_idx in range(len(matrix_[row_idx])):
            if matrix_[row_idx][col_idx] == element:
                return row_idx, col_idx


rows = int(input())

matrix = []

for _ in range(rows):
    current_list = list(input())
    matrix.append(current_list)

searched_symbol = input()
position = find_element(matrix, searched_symbol)

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
