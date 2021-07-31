import math

a = int(input())
b = int(input())
n = int(input())

ans = a * b / math.gcd(a, b)

if ans >= n:
    print(int(ans))
    exit()
else:
    while ans < n or ans % a != 0 or ans % b != 0:
        ans += min(a, b)

print(int(ans))
