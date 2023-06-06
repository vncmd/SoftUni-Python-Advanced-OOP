nums_seq = []


def create_sequence(number):
    nums_seq.clear()
    nums_seq.append(0)
    nums_seq.append(1)

    for _ in range(number - 2):
        nums_seq.append(nums_seq[-1] + nums_seq[-2])

    return ' '.join(map(str, nums_seq))


def locate_number(num):
    if num in nums_seq:
        element_index = nums_seq.index(num)
        return f'The number - {num} is at index {element_index}'
    else:
        return f'The number {num} is not in the sequence'
