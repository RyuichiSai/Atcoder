S = input()
N = int(input())

L = []

for i in range(5):
    for j in range(5):
        L.append(S[i] + S[j])

print(L[N - 1])
