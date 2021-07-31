s = input()
k = int(input())
L = []

for i in range(len(s) - k + 1):
    L.append(s[i:k + i])

if len(s) < k:
    print(0)
else:
    print(len(set(L)))
