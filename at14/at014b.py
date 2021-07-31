N, X = map(int, input().split())
a = list(map(int, input().split()))

s = 0

for i, v in enumerate(a):
    if X & (1 << i):
        s += v

print(s)
