def main():
    s = input()
    a = s[:2]
    b = s[2:]

    az = int(a) == 0
    ap = 0 < int(a) < 100
    am = 0 < int(a) < 13
    bz = int(b) == 0

    bp = 0 < int(b) < 100
    bm = 0 < int(b) < 13
    if ap and am and bp and bm:
        print('AMBIGUOUS')
    elif ap and am and (bz or bp) and not bm:
        print('MMYY')
    elif (az or ap) and not am and bp and bm:
        print('YYMM')
    else:
        print('NA')


main()
