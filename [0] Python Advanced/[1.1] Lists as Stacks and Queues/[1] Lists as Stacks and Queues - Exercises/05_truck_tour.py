from collections import deque

petrol_pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

copied_pumps = petrol_pumps.copy()
gas_tank = 0
idx = 0

while copied_pumps:
    petrol, distance = copied_pumps.popleft()

    gas_tank += petrol

    if gas_tank >= distance:
        gas_tank -= distance
    else:
        petrol_pumps.rotate(-1)
        copied_pumps = petrol_pumps.copy()
        idx += 1
        gas_tank = 0

print(idx)
