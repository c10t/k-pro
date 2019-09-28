from operator import itemgetter


def main():
    n, m = list(map(int, input().split()))
    alist = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b, c = list(map(int, input().split()))
        bc.append((b, c))

    asorted = sorted(alist)

    bc = sorted(bc, key=itemgetter(1), reverse=True)

    # print(f'initial: {asorted}')
    # print(f'bc: {bc}')

    fixed = []
    for b, c in bc:
        pick = [a for a in asorted if a >= c]

        if len(pick) > 0:
            asorted = asorted[:-len(pick)]
            fixed += pick

        if len(asorted) < 1:
            break

        for _ in range(b):
            if len(asorted) < 1:
                break
            asorted.pop(0)
            fixed.insert(0, c)

        # print(f'--- step n / {len(bc)} ---')
        # print(f'asorted: {asorted}')
        # print(f'pick   : {pick}')
        # print(f'fixed  : {fixed}')

    fixed += asorted

    print(sum(fixed))


main()
