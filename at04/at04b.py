N = [list(map(str, input().split(" "))) for i in range(4)]

N.reverse()

for i in range(4):
    N[i].reverse()

for i in range(4):
    print(*N[i])
