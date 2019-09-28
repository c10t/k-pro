s = input()
t = input()

count = 0
for forecast, actual in zip(s, t):
    if forecast == actual:
        count += 1

print(count)
