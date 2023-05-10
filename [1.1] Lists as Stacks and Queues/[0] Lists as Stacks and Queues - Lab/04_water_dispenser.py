from collections import deque

people = deque()

quantity_water = int(input())

data_names = input()
while data_names != "Start":
    people.append(data_names)

    data_names = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        wanted_lt = int(data[0])

        if quantity_water >= wanted_lt:
            quantity_water -= wanted_lt
            person = people.popleft()
            print(f"{person} got water")

        else:
            person = people.popleft()
            print(f"{person} must wait")

    else:
        liters_to_fill = int(data[1])
        quantity_water += liters_to_fill

    command = input()

print(f"{quantity_water} liters left")
