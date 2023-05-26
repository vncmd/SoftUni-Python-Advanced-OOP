def func_executor(*funcs):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in funcs])


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
