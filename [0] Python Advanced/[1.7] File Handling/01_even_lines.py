def get_even_lines_from_text_file(file_name):
    with open(file_name) as file:
        data = file.readlines()
        result = [data[i][:-1] for i in range(len(data)) if i % 2 == 0]

    return result


def replace_chars_with_at_symbol(data):
    for i in range(len(data)):
        for char in special_chars:
            if char in data[i]:
                data[i] = data[i].replace(char, special_symbol)


def change_word_order(data):
    result = [line.split()[::-1] for line in data]
    return result


def format_lines(data):
    replace_chars_with_at_symbol(data)
    result = change_word_order(data)

    return result


def print_result(data):
    for line in data:
        print(" ".join(line))


special_chars = ["-", ",", ".", "!", "?"]
special_symbol = "@"

n_lines = get_even_lines_from_text_file("text.txt")

formatted_lines = format_lines(n_lines)

print_result(formatted_lines)
