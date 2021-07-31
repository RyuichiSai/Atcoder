N, S, T = map(int, input().split())
W = int(input())
A = [int(input()) for i in range(N - 1)]

cnt = 0
if W >= S and W <= T:
    cnt += 1

for i in range(N-1):
    W += A[i]
    if W >= S and W <= T:
        cnt += 1
    else:
        pass

print(cnt)
