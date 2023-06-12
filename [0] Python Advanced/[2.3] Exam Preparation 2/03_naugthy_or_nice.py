def naughty_or_nice(santa_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.append(kids[0][1]) if kid_type == "Nice" else naughty_kids.append(kids[0][1])
            santa_list.remove(*kids)

    for kid_data in args:
        num, kid_type = kid_data.split("-")

        kids = [info for info in santa_list if info[0] == int(num)]

        place_kid()

    for name, kid_type in kwargs.items():
        kids = [data for data in santa_list if data[1] == name]

        place_kid()

    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")

    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")

    if santa_list:
        result.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return "\n".join(result)
