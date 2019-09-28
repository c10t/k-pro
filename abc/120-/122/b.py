s = input()

acgt = {"A", "C", "G", "T"}
converted = ""
for char in s:
    if char in acgt:
        converted += "1"
    else:
        converted += " "

substrs = [len(substr) for substr in converted.split()]
answer = 0 if len(substrs) < 1 else max(substrs)
print(answer)
