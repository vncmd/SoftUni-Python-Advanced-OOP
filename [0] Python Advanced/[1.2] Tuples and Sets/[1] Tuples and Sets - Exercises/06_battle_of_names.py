odd = set()
even = set()

data_lines = int(input())
for row in range(1, data_lines + 1):
    ascii_sum = sum(ord(letter) for letter in input()) // row

    if ascii_sum % 2 == 0:
        even.add(ascii_sum)
    else:
        odd.add(ascii_sum)

if sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
else:
    print(*odd.symmetric_difference(even), sep=", ")
