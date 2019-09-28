def main():
    s = input()

    # split into sub-problems: 'RRLRL' => 'RRL', 'RL'
    subprob = []
    substr = ''
    for i in range(len(s)):
        substr += s[i]
        # print(i, s[i])

        if i == len(s) - 1:
            subprob.append(substr)
            break

        if s[i] == 'L' and s[i + 1] == 'R':
            subprob.append(substr)
            substr = ''

    # print(subprob)

    answer = []
    for subp in subprob:
        r = subp.count('R')
        l = subp.count('L')

        border = 0
        for i in range(len(subp) - 1):
            if subp[i] == 'R' and subp[i + 1] == 'L':
                # R ... R | L ... L
                border = i

        quotient = len(subp) // 2
        reminder = len(subp) % 2
        if border % 2 == 0:
            answer += [0] * (r - 1)
            answer += [quotient + reminder] + [quotient]
            answer += [0] * (l - 1)
        else:
            answer += [0] * (r - 1)
            answer += [quotient] + [quotient + reminder]
            answer += [0] * (l - 1)

    print(' '.join(map(str, answer)))


main()
