from itertools import combinations

antenna = []
for _ in range(5):
    antenna.append(int(input()))
k = int(input())

answer = "Yay!"
for x, y in combinations(antenna, 2):
    if abs(x - y) > k:
        answer = ":("
        break
print(answer)
