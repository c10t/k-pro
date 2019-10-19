n = int(input())
s = input()

compressed = s[0]
for i in range(1, n):
    if s[i] != s[i - 1]:
        compressed += s[i]

print(len(compressed))
