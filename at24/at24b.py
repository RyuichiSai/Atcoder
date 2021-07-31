N, T = map(int, input().split())
a = [int(input()) for i in range(N)]
ans = T

for i in range(N - 1):
    if a[i + 1] - a[i] < T:
        ans += a[i + 1] - a[i]
    else:
        ans += T

print(ans)
