def main():
    n = int(input())

    edges = []
    for _ in range(n - 1):
        u, v, w = list(map(int, input().split()))
        edges.append((u, v, w))

    # print(edges)
    edges = [(u, v) for u, v, w in edges if w % 2 != 0]
    # print(edges)

    has_odd = set(list(sum(edges, ())))
    # print(has_odd)

    if len(edges) < 1:
        for i in range(1, n + 1):
            print('0')
        return

    remain = edges
    b = []
    w = []
    u1, v1 = remain.pop(0)
    b.append(u1)
    w.append(v1)

    must_black = [u1]
    must_white = [v1]

    step = []
    while len(remain) > 0:
        u1, v1 = remain.pop(0)
        if u1 in must_black:
            b.append(u1)
            w.append(v1)
            if v1 not in must_white:
                must_white.append(v1)
        elif v1 in must_black:
            b.append(v1)
            w.append(u1)
            if u1 not in must_white:
                must_white.append(u1)
        elif u1 in must_white:
            b.append(v1)
            w.append(u1)
            if v1 not in must_black:
                must_black.append(v1)
        elif v1 in must_white:
            b.append(u1)
            w.append(v1)
            if u1 not in must_black:
                must_black.append(u1)
        else:
            step.append((u, v))

        if len(remain) < 1 and len(step) > 0:
            new_u1, new_v1 = step.pop(0)
            b.append(new_u1)
            w.append(new_v1)
            must_white.append(new_v1)
            must_black.append(new_u1)
            remain = step

    b = set(b)
    w = set(w)
    b = [{'c': 1, 'n': elem} for elem in b]
    w = [{'c': 0, 'n': elem} for elem in w]
    z = [{'c': 0, 'n': i} for i in range(1, n + 1) if i not in has_odd]
    result = sorted(b + w + z, key=lambda x: x['n'])
    # print(result)
    for e in result:
        print(e['c'])


main()
