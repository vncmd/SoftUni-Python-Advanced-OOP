def sorting_cheeses(**kwargs):
    result = ""

    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )
    for name, quantity in sorted_cheeses:
        result += name + "\n"

        sorted_quantities = sorted(quantity, reverse=True)

        result += "\n".join(str(el) for el in sorted_quantities) + "\n"

    return result
