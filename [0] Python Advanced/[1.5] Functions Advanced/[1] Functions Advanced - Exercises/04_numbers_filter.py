def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [n for n in kwargs["odd"] if n % 2 != 0]

    if "even" in kwargs:
        kwargs["even"] = [n for n in kwargs["even"] if n % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
