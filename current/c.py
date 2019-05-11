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

        has_A_rs = word.endsWith('A')
        # has_B_rs = word.endsWith('B')
        # has_A_ls = word.startsWith('A')
        has_B_ls = word.startsWith('B')

        categorized.append({
            'w': word, '#': idt, 'itself': itself,
            'rA': has_A_rs, 'lB': has_B_ls
        })

        # lXrX = [w for w in categorized if not w['rA'] and not w['rB']]
        lBrA = len([w for w in categorized if w['rA'] and w['rB']])
        lBrX = len([w for w in categorized if not w['rA'] and w['rB']])
        lXrA = len([w for w in categorized if w['rA'] and not w['rB']])

        s = sum([w['itself'] for w in categorized])
        if lBrA == 0:
            s += min(lBrX, lXrA)
        else:
            if lBrX == lXrA:
                s += lBrX + (lBrA - 1)
            else:
                pass

        print(s)


if __name__ == '__main__':
    # s = perf_counter()
    main()
    # e = perf_counter()
    # print('process:', e - s)
