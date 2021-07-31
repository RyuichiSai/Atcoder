S = list(input())
N = int(input())

lr = [map(int, input().split()) for _ in range(N)]
l, r = [list(i) for i in zip(*lr)]

for i in range(N):
    S[l[i] - 1:r[i]] = reversed(S[l[i] - 1:r[i]])

print("".join(S))
