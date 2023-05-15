from collections import deque

green_time = int(input())
yellow_time = int(input())

total_cars = 0

cars = deque()
data = input()

while data != "END":
    if data != "green":
        cars.append(data)
    else:
        current_green = green_time

        while current_green > 0 and cars:
            car = cars.popleft()
            time = current_green + yellow_time

            if len(car) > time:
                print(f"A crash happened!\n{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            total_cars += 1

    data = input()

print(f"Everyone is safe.\n{total_cars} total cars passed the crossroads.")
