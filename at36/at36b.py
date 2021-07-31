N = int(input())
s = [input() for _ in range(N)]
ss = [""]*N

for i in range(N-1, -1, -1):
    for j in range(N):
        ss[j] += s[i][j]

print(*ss, sep="\n")
