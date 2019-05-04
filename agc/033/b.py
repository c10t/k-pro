def main():
    h, w, n = list(map(int, input().split()))
    sr, sc = list(map(int, input().split()))
    s = input()
    t = input()

    sx = s.replace('U', 'X').replace('D', 'X')
    sy = s.replace('L', 'X').replace('R', 'X')
    tx = t.replace('U', 'X').replace('D', 'X')
    ty = t.replace('L', 'X').replace('R', 'X')

    current = sr
    for si, ti in zip(sx, tx):
        if si == 'X':
            pass
        elif si == 'L':
            if current < 1:
                print('NO')
                return
        elif si == 'R':

            pass
        if current < 0 or current > w - 1:
            print('NO')
            return

    current = sc
    for si, ti in zip(sy, ty):
        if current < 0 or current > h - 1:
            print('NO')
            return


main()
