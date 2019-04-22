def main():
    s = input()
    ops = [i for i in range(len(s) - 1)]

    powset = []
    for i in range(1 << len(ops)):
        powset.append([ops[j] for j in range(len(ops)) if ((i >> j) & 1) == 1])

    # print(powset)

    expressions = []
    for places in powset:
        f = ''
        for i, char in enumerate(s):
            if i in places:
                f += char + '+'
            else:
                f += char
        expressions.append(f)

    # print(expressions)

    total = sum(map(eval, expressions))
    print(total)


main()
