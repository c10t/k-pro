alphabet = "abcdefghijklmnopqrstuvwxyz"

c = input().strip()

for i, char in enumerate(alphabet):
    if char == c:
        print(alphabet[i + 1])
