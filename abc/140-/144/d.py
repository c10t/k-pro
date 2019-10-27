import math

a, b, x = list(map(int, input().split()))

x /= a  # focus on the rectangle a * b

if a * b / 2 > x:
    c = 2 * x / b
    answer = math.degrees(math.atan2(b / c))
    print(answer)
else:
    rest = a * b - x
    c = 2 * rest / a
    answer = math.degrees(math.atan2(c / a))
    print(answer)
