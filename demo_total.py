def total(xs):
    if not xs:
        return 0.0
    s = 0
    for i in range(len(xs)):
        s += xs[i]
    return float(s)
