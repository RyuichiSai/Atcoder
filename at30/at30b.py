
n, m = map(int, input().split())

if n >= 12:
    n -= 12
    n = 360 * ((n + (m / 60)) / 12)
elif n == 0:
    n = 360 * ((m / 60) / 12)
else:
    n = 360 * ((n + (m / 60)) / 12)

if m == 0:
    pass
else:
    m = 360 * (m / 60)

d = 360 - abs(n - m)

if d <= abs(n - m):
    print(d)
else:
    print(abs(n - m))
