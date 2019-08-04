from collections import defaultdict

MOD = 1000000007


def main():
    n, m = list(map(int, input().split()))
    stairs = defaultdict(lambda: True)
    for i in range(m):
        a = int(input())
        stairs[a] = False

    dp = defaultdict(lambda: 0)
    dp[0] = 1

    for i in range(1, n + 1):
        if stairs[i]:
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] %= MOD

    print(dp[n])


main()
