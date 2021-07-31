N = int(input())
a = list(map(int, input().split()))
cnt = 0
s = 0
if sum(a) % N >= 1:
    print(-1)
elif len(set(a)) == 1:
    print(0)
else:
    for i in range(N):
        s += a[i]
        if s != (sum(a) / N) * (i + 1):
            cnt += 1
        elif a[i] > sum(a) / len(a):
            pass

    print(cnt)
