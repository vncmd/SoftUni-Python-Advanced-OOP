from custom_module.fibonacci_sequence import create_sequence, locate_number

operations = {
    "Create": create_sequence,
    "Locate": locate_number
}

command = input()
while command != "Stop":

    operation, *data = command.split()
    print(operations[operation](int(data[-1])))

    command = input()
