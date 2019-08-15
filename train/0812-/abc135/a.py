a, b = list(map(int, input().split()))
answer = "IMPOSSIBLE" if (a + b) % 2 == 1 else str((a + b) // 2)
print(answer)
