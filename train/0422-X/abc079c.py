

def find(abcd):
    a, b, c, d = abcd
    ops = ['{}{}{}'.format(i, j, k)
           for i in [1, 2] for j in [1, 2] for k in [1, 2]]
    opr = {'1': '+', '2': '-'}

    for op in ops:
        expression = a + opr[op[0]] + b + opr[op[1]] + c + opr[op[2]] + d
        try:
            if eval(expression) == 7:
                return(expression)
        except SyntaxError:
            pass


def main():
    abcd = input()
    print('{}=7'.format(find(abcd)))


main()
