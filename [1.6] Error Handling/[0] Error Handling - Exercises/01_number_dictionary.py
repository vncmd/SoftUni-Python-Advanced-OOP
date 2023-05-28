numbers = {}

data = input()

while data != "Search":
    try:

        num_as_str = data
        number = int(input())
        numbers[num_as_str] = number

    except ValueError:
        print("The variable number must be an integer")

    data = input()

data = input()

while data != "Remove":
    try:

        searched = data
        print(numbers[searched])

    except KeyError:
        print("Number does not exist in dictionary")

    data = input()

data = input()

while data != "End":
    try:

        searched = data
        del numbers[searched]

    except KeyError:
        print("Number does not exist in dictionary")

    data = input()

print(numbers)
