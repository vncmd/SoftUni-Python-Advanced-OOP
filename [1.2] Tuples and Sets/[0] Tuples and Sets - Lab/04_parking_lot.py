n = int(input())
cars = set()

for _ in range(n):
    command, num = input().split(", ")
    if command == "IN":
        cars.add(num)
    elif command == "OUT":
        cars.remove(num)

if cars:
    print(*cars, end="\n")
else:
    print("Parking Lot is Empty")
