# https://www.codewars.com/kata/555b1890a75b930e63000023/train/python
c = set()


def combos(n):
    global c
    process(n, [])
    out = [list(i) for i in c]
    c = set()
    return out


def process(d, s):
    global c
    if d == 0:
        c.add(tuple(sorted(s)))
        return None
    else:
        for i in range(1, d + 1):
            process(d - i, s + [i])