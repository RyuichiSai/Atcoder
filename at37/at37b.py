N, Q = map(int, input().split())
LRT = [list(map(int, input().split())) for _ in range(Q)]
a = [0]*N
for i in range(Q):
    for j in range(LRT[i][0] - 1, LRT[i][1]):
        a[j] = LRT[i][2]
for i in a:
    print(i)
