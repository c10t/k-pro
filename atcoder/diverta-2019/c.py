# from time import perf_counter


def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    categorized = []
    for word in words:
        idt = len(categorized)
        itself = word.count('AB')

        has_A_rs = word.endswith('A')
        # has_B_rs = word.endsWith('B')
        # has_A_ls = word.startsWith('A')
        has_B_ls = word.startswith('B')

        categorized.append({
            'w': word, '#': idt, 'itself': itself,
            'rA': has_A_rs, 'lB': has_B_ls
        })

    # lXrX = [w for w in categorized if not w['rA'] and not w['rB']]
    lBrA = len([w for w in categorized if w['rA'] and w['lB']])
    lBrX = len([w for w in categorized if not w['rA'] and w['lB']])
    lXrA = len([w for w in categorized if w['rA'] and not w['lB']])

    s = sum([w['itself'] for w in categorized])
    if lBrA == 0:
        s += min(lBrX, lXrA)
    elif lBrX + lXrA > 0:
        s += lBrA + min(lBrX, lXrA)
    else:
        s += lBrA - 1

    print(s)


if __name__ == '__main__':
    # s = perf_counter()
    main()
    # e = perf_counter()
    # print('process:', e - s)
