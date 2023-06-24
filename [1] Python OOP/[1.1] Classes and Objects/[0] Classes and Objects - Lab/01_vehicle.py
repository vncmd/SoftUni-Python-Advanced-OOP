class Vehicle:
    def __init__(self, mileage: float, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


# Tests:

car = Vehicle(20)

print(car.max_speed)
print(car.mileage)
print(car.gadgets)

car.gadgets.append('Cup holder')
print(car.gadgets)
