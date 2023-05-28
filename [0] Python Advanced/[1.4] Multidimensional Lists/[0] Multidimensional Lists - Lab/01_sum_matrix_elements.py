rows, cols = [int(el) for el in input().split(", ")]

matrix = []
sum_nums = 0

for _ in range(rows):
    current_list = [int(el) for el in input().split(", ")]
    sum_nums += sum(current_list)
    matrix.append(current_list)

print(sum_nums)
print(matrix)
