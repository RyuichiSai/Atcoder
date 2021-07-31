A, B, C, K = map(int, input().split())
S, T = map(int, input().split())
w = 0

if S + T >= K:
    w = (S + T) * C
else:
    pass

print((A * S) + (B * T) - w)
