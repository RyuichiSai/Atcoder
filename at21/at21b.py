import sys

N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

P = list(set(P))

for i in range(len(P)):
    if P[i] == a or P[i] == b:
        print("NO")
        sys.exit()
    else:
        pass

if len(P) == K:
    print("YES")
else:
    print("NO")
