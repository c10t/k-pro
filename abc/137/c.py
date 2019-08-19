def main(ss):
    sorted_ss = ["".join(sorted(s)) for s in ss]
    # print(sorted_ss)
    visited = dict()
    count = 0
    for s in sorted_ss:
        if s in visited:
            count += visited[s]
            visited[s] += 1
        else:
            visited[s] = 1

    return count


n = int(input())
ss = []
for _ in range(n):
    ss.append(input())

print(main(ss))
