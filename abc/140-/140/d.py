a, b = list(map(int, input().split()))


def prime_factorize(n):
    """Return the prime factorization of n > 1.
    >>> prime_factorize(36)
    [2, 2, 3, 3]
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    return a


def main(a, b):
    pf_a = set(prime_factorize(a))
    pf_b = set(prime_factorize(b))
    return len(pf_a & pf_b) + 1


print(main(a, b))

# for i in range(2, min(a, b) + 1):
#     if a % i != 0 or b % i != 0:
#         continue
#     if not any([i % x == 0 for x in cands]):
#         cands.add(i)

# print(len(cands) + 1)

# def comdiv(n, m):
#     cds = []  # exclude 1
#     for i in range(2, min(n, m) + 1):
#         if n % i == 0 and m % i == 0:
#             cds.append(i)

#     return sorted(cds)


# def main(a, b):
#     cds = comdiv(a, b)
#     cand = set()

#     for cd in cds:
#         if len(cand) == 0:
#             cand.add(cd)
#             continue
#         if all([cd % x != 0 for x in cand]):
#             cand.add(cd)

#     return len(cand) + 1


# print(main(a, b))
