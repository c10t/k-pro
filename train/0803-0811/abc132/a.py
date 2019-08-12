from collections import Counter

s = input()
sc = Counter(s)

a = 'Yes'
for i in sc.keys():
    if sc[i] != 2:
        a = 'No'
        break

print(a)
