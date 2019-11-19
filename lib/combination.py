MOD = 10 ** 9 + 7


def combination(n, r, mod=10 ** 9 + 7):
    """
    r ~ n/2 だと遅くなる
    >>> combination(666666, 333333)
    151840682
    """
    n1, r = n + 1, min(r, n - r)
    numerator = denominator = 1
    for i in range(1, r + 1):
        numerator = numerator * (n1 - i) % mod
        denominator = denominator * i % mod

    return numerator * pow(denominator, mod - 2, mod) % mod


class Combination:
    """
    初期化時に O(N) の計算を行っておくことで O(1) で nCk (mod MOD) の計算を行える

    >>> cmb = Combination(2000)
    >>> cmb(5, 3) % MOD
    10
    """

    def __init__(self, N):
        self.fact = [1] * (N + 1)

        for i in range(1, N + 1):
            self.fact[i] = (self.fact[i - 1] * i) % MOD

        self.invmod = [1] * (N + 1)
        self.invmod[N] = pow(self.fact[N], MOD - 2, MOD)

        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % MOD

    def __call__(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        elif n == 0 or k == 0 or n == k:
            return 1
        else:
            return self.fact[n] * (self.invmod[k] % MOD) * (self.invmod[n - k] % MOD)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
