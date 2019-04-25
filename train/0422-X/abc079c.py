def main():
    abcd = input()
    ops = [i for i in range(len(abcd) - 1)]

    powset = []
    for i in range(1 << len(ops)):
        powset.append([ops[j] for j in range(len(ops)) if ((i >> j) & 1) == 1])

    result = ''
    for places in powset:
        expressions = []
        for i, char in enumerate(s):
            if i in places:
                f += char + '+'
            else:
                f += char
        expressions.append(f)
        checklist = list(map(eval, expressions))

    print(result)
