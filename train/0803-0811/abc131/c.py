def gcd(n, m):
    x = max(n, m)
    y = min(n, m)

    while y != 0:
        x, y = y, x % y

    return x


def main():
    a, b, c, d = list(map(int, input().split()))

    # count of factors of c which are less than or equal to b
    fclb = b // c
    # count of factors of d which are less than or equal to b
    fdlb = b // d

    # least common multiple
    lcm = c * d // gcd(c, d)  # greatest common divisor

    duplicated_b = b // lcm
    count_b = b - fclb - fdlb + duplicated_b

    fcla = (a - 1) // c
    fdla = (a - 1) // d
    duplicated_a = (a - 1) // lcm
    count_a = (a - 1) - fcla - fdla + duplicated_a

    score = count_b - count_a
    print(score)


main()
