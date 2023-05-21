data = input().split("|")

sub_lists = []

for sub_string in data[::-1]:
    sub_lists.extend(sub_string.split())


print(*sub_lists)
