row = int(input())

matrix = []
sum_nums = 0

for row_idx in range(row):
    current_list = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(current_list)

print(matrix)
