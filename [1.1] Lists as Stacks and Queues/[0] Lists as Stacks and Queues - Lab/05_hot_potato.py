from collections import deque

data_names = deque(input().split())
n_rotation = int(input()) - 1

while len(data_names) > 1:
    data_names.rotate(-n_rotation)
    name_to_leave = data_names.popleft()
    print(f"Removed {name_to_leave}")

print(f"Last is{data_names.popleft()}")
