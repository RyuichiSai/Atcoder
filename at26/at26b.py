import math

N = int(input())
R = [int(input()) for i in range(N)]
R.sort()
a = 0
for i in range(N):
    if i % 2 == 0:
        a += R[i]**2
    else:
        a -= R[i]**2
ans = a*math.pi
print(abs(ans))
