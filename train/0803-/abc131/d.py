from operator import itemgetter


def main():
    n = int(input())
    ab = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        ab.append((a, b))

    ab = sorted(ab, key=itemgetter(1))

    acc = 0
    answer = 'Yes'
    for a, b in ab:
        acc += a
        if acc > b:
            answer = 'No'
            break

    print(answer)


main()
