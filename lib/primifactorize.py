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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
