def main(n, a):
    box = [0] * n
    for i in range(n, 0, -1):
        if a[i - 1] != sum(box[i - 1 :: i]) % 2:
            box[i - 1] = 1

    box_indices = [i + 1 for i in range(n) if box[i] == 1]
    print(sum(box))
    print(*box_indices)


n = int(input())
a = list(map(int, input().split()))
main(n, a)
