deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}

directions = {
    "left": lambda r, c: [r, (c - 1) % SIZE],
    "right": lambda r, c: [r, (c + 1) % SIZE],
    "up": lambda r, c: [(r - 1) % SIZE, c],
    "down": lambda r, c: [(r + 1) % SIZE, c],
}

mars_land = []
rover_coord = []
SIZE = 6

for row in range(SIZE):
    current_row = input().split()

    if "E" in current_row:
        rover_coord = [row, current_row.index("E")]

    mars_land.append(current_row)

commands = input().split(", ")

for command in commands:
    rover_coord = directions[command](*rover_coord)
    position = mars_land[rover_coord[0]][rover_coord[1]]

    if position in deposits:
        print(f"{deposits[position][0]} deposit found at ({rover_coord[0]}, {rover_coord[1]})")

        deposits[position][1] += 1

    elif position == "R":
        print(f"Rover got broken at ({rover_coord[0]}, {rover_coord[1]})")

        break

if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
    print("Area suitable to start the colony.")

else:
    print("Area not suitable to start the colony.")
