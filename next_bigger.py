# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
def next_bigger(n):
    list = [int(i) for i in str(n)]
    spisek = []
    indexrep = 0
    for i in range(2, len(list) + 1):
        for c in range(1, i):
            if list[-i] < list[-c]:
                indexrep = -i
                spisek.append(list[-c])
        if len(spisek) != 0:
            break
    if len(spisek) == 0:
        return -1

    value = sorted(spisek)[0]
    first = list[:indexrep]
    second = list[indexrep:]

    first.append(value)
    second.remove(value)
    second.sort()
    first.extend(second)



    out = ""

    for item in first:
        out += str(item)
    if out[0] == '0':
        return -1
    return int(out)