def fibonacci():
    num_one, num_two = 0, 1

    while True:
        yield num_one

        num_one, num_two, = num_two, num_one + num_two


generator = fibonacci()
for i in range(500):
    print(next(generator))
