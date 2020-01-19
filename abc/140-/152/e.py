from fractions import gcd
from functools import reduce

MOD = 10 ** 9 + 7


def lcm(*nums):
    return reduce(lambda x, y: (x * y) // gcd(x, y), nums, 1)


# print(lcm(*[2, 3, 4])) -> 12

n = int(input())
a = list(map(int, input().split()))

l = lcm(*a)
ans = 0

for ai in a:
    ans += l // ai

print(ans % MOD)
