W, H, N = map(int, input().split())
xya = [map(int, input().split()) for _ in range(N)]
x, y, a = [list(i) for i in zip(*xya)]

max_1x = 0
min_2x = W
max_3y = 0
min_4y = H

for i in range(N):
    if a[i] == 1:
        if x[i] > max_1x:
            max_1x = x[i]
        else:
            pass
    elif a[i] == 2:
        if x[i] < min_2x:
            min_2x = x[i]
        else:
            pass
    elif a[i] == 3:
        if y[i] > max_3y:
            max_3y = y[i]
        else:
            pass
    elif a[i] == 4:
        if y[i] < min_4y:
            min_4y = y[i]
        else:
            pass

if min_2x > max_1x and min_4y > max_3y:
    print((min_2x - max_1x) * (min_4y - max_3y))
else:
    print(0)
