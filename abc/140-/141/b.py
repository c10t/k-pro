s = input().strip()

answer = "Yes"

for i in range(len(s)):
    if i % 2 == 0 and s[i] == "L":
        answer = "No"
        break
    if i % 2 == 1 and s[i] == "R":
        answer = "No"
        break

print(answer)
