n = int(input())
reservations = set()

for _ in range(n):
    n_reservations = input()
    reservations.add(n_reservations)

guest = input()
while guest != "END":
    if guest in reservations:
        reservations.remove(guest)

    guest = input()

print(len(guest))

for num in sorted(reservations):
    print(num)
