N = int(input())
T = tuple(map(int, input().split()))
M = int(input())
PX = [map(int, input().split()) for _ in range(M)]
P, X = [list(i) for i in zip(*PX)]


for i in range(M):
    a = list(T)
    a[P[i] - 1] = X[i]
    print(sum(a))
