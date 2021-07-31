N = int(input())
a = N // 2
b = N % 2

ans = list(range(a + b))

for i in range(a):
    ans[i] = 2

if b == 1:
    ans[a + b - 1] = 1

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
