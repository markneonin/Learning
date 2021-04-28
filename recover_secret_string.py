# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python
from collections import defaultdict as dd


def recoverSecret(s):
    d = dd(list)
    o = dd(list)
    l = {}
    for l1, l2, l3 in s:
        o[l1].append(l2)
        o[l1].append(l2)
        l[l1] = 0

        d[l2].append(l1)
        o[l2].append(l3)
        l[l2] = 0

        d[l3].append(l2)
        d[l3].append(l1)
        l[l3] = 0

    for k, v in d.items():
        d[k] = set(v)
    for k, v in o.items():
        o[k] = set(v)
    sp = []

    for k, v in l.items():
        if k not in d:
            sp.append(k)

    while len(sp) < len(l):
        for k in l.keys():
            if k not in sp:
                flag = True
                for i in d[k]:
                    if i not in sp:
                        flag = False
                if flag:
                    sp.append(k)
            else:
                pass
    return ''.join(sp)