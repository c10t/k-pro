# from time import perf_counter


def main():
    r, g, b, n = list(map(int, input().split()))
    count = 0
    x1, x2, x3 = sorted([r, g, b], reverse=True)
    # print(x1, x2, x3)
    for i in range(n // x1 + 1):
        for j in range((n - i) // x2 + 1):
            rest = n - (x1 * i) - (x2 * j)
            # print(f'{x1}*{i} + {x2}*{j} = {n - rest}')
            if rest == 0:
                # print(f'{x1}*{i} + {x2}*{j} + {x3}*0 = {n}')
                count += 1
            else:
                # print(f'{x1}*{i} + {x2}*{j} + {x3}*? = {n}')
                count += (1 if rest > 0 and rest % x3 == 0 else 0)
            # for k in range((n - i - j) // x3 + 1):
                # print(f'{r}*{i} + {g}*{j} + {b}*{k} = {r*i+g*j+k+b*k}')
            #    if x1 * i + x2 * j + x3 * k == n:
            #        count += 1

    print(count)


if __name__ == '__main__':
    # s = perf_counter()
    main()
    # e = perf_counter()
    # print('process:', e - s)
