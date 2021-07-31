L, H = map(int, input().split())
N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N):
    if L <= A[i] and H >= A[i]:
        print(0)
    elif A[i] < L:
        print(L - A[i])
    else:
        print(-1)
