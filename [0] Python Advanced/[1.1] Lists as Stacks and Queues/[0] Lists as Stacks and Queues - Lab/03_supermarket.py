from collections import deque

customers = deque()

while True:
    data = input()
    if data == "Paid":
        while customers:
            print(customers.popleft())

        continue

    elif data == "End":
        break

    customers.append(data)

print(f"{len(customers)} people remaining.")
