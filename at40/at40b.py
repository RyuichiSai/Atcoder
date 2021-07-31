n = int(input())

ans = [10100] * 100100
a = [10100] * 100100
h = 1
w = n

for i in range((n // 2) + 1):
    ans[i] = abs(h - w) + (n % (w * h))
    a[i] = n % (w * h)
    h += 1
    w = n // h


print(min(ans))
