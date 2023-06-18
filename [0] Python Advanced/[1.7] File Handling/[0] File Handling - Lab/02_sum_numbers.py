def numbers_sum(file_name):
    data = open(file_name, 'r')
    sum_nums = 0

    for number in data:
        sum_nums += int(number)

    return sum_nums


result = numbers_sum('text.txt')
print(result)
