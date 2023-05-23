def recursive_power(num, n_power):
    if n_power == 1:
        return num
    return num * recursive_power(num, n_power - 1)
