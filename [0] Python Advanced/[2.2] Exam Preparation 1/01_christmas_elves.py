from collections import deque

elf_energy = deque(int(x) for x in input().split())
n_materials = [int(x) for x in input().split()]

energy_used = 0
toys_created = 0
turns_count = 0

while elf_energy and n_materials:
    while elf_energy and elf_energy[0] < 5:
        elf_energy.popleft()

    if not elf_energy:
        break

    materials = n_materials.pop()
    energy = elf_energy.popleft()

    turns_count += 1
    toys_to_be_created = 1
    energy_spent = materials
    energy_increase = 1

    if turns_count % 3 == 0:
        toys_to_be_created = 2
        energy_spent *= 2

    if turns_count % 5 == 0:
        toys_to_be_created = 0
        energy_increase = 0

    if energy >= energy_spent:
        toys_created += toys_to_be_created
        energy_used += energy_spent
        elf_energy.append(energy - energy_spent + energy_increase)

    else:
        n_materials.append(materials)
        elf_energy.append(energy * 2)

print(f'Toys: {toys_created}')
print(f'Energy: {energy_used}')

if elf_energy:
    print(f'Elves left: {", ".join([str(x) for x in elf_energy])}')
if n_materials:
    print(f'Boxes left: {", ".join([str(x) for x in n_materials])}')
