rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    current_list = [int(el) for el in input().split(", ")]
    matrix.append(current_list)

max_sum = float("-inf")

sub_matrix = []
for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        current_el = matrix[row_idx][col_idx]
        below_el = matrix[row_idx + 1][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        diagonal_el = matrix[row_idx + 1][col_idx + 1]
        elements_sum = current_el + below_el + next_el + diagonal_el

        if max_sum < elements_sum:
            max_sum = elements_sum
            sub_matrix = [[current_el, next_el], [below_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
