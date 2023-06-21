nums_list = [int(x) for x in input().split(", ")]

result = 1

for idx in range(len(nums_list)):
    number = nums_list[idx]

    if number <= 5:
        result *= number

    elif 5 < number <= 10:
        result /= number

print(result)
