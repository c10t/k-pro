dish = []
for _ in range(5):
    dish.append(int(input()))

dish1 = [x for x in dish if x % 10 == 0]
dish2 = [x for x in dish if x % 10 != 0]
dish2 = sorted(dish2, key=lambda x: x % 10, reverse=True)

score = sum(dish1)
for i, d in enumerate(dish2):
    if i < len(dish2) - 1:
        score += d + (10 - d % 10)
    else:
        score += d

print(score)
