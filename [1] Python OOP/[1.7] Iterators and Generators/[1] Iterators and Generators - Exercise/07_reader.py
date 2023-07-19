def read_next(*args):
    idx = 0

    while idx < len(args):
        for item in args[idx]:
            yield item

        idx += 1
