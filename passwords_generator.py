# Само задание:
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
slovar = {
    0: (0, 8),
    1: (1, 2, 4),
    2: (1, 2, 3, 5),
    3: (2, 3, 6),
    4: (1, 4, 5, 7),
    5: (2, 4, 5, 6, 8),
    6: (3, 5, 6, 9),
    7: (4, 7, 8),
    8: (5, 7, 8, 9, 0),
    9: (9, 8, 6)
}


def chiselka(lenght, ilist):
    list = [i - 1 for i in ilist]
    slovar = {}
    for i in range(lenght):
        slovar[i] = 0
    yield slovar
    while True:
        for i in range(lenght):
            if slovar[i] < list[i]:
                slovar[i] += 1
                break
            else:
                if slovar[i + 1] < list[i + 1]:
                    for c in range(i + 1):
                        slovar[c] = 0
                    slovar[i + 1] += 1
                    break
        yield slovar


def get_pins(observed):
    spisek = [int(i) for i in list(observed)]
    value = 1
    for a in spisek:
        value *= len(slovar[a])
    variations = [len(slovar[i]) for i in spisek]
    generator = chiselka(len(spisek), variations)
    out = []

    for i in range(value):
        var = next(generator)
        var_str = ''
        for item in var:
            var_str += str(slovar[spisek[item]][var[item]])
        out.append(var_str)
    return out
