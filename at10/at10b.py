n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] == 1 or a[i] == 3 or a[i] == 7 or a[i] == 9:
        a[i] = 0
    elif a[i] == 2 or a[i] == 4 or a[i] == 8 or a[i] == 10:
        a[i] = 1
    elif a[i] == 5:
        a[i] = 2
    else:
        a[i] = 3

print(sum(a))
