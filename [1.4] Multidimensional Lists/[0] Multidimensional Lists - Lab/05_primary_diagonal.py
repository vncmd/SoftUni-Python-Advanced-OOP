rows = int(input())

matrix = []

for _ in range(rows):
    current_list = [int(el) for el in input().split()]
    matrix.append(current_list)

diagonal_sum = 0
for idx in range(rows):
    diagonal_sum += matrix[idx][idx]

print(diagonal_sum)
