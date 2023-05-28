num = int(input())
matrix = [[int(n) for n in input().split()] for row in range(num)]

primary_sum = 0
secondary_sum = 0

for idx in range(num):
    primary_sum += matrix[idx][idx]
    secondary_sum += matrix[idx][num - idx - 1]

print(abs(primary_sum - secondary_sum))
