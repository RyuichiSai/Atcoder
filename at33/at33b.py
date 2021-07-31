N = int(input())
list = []
for i in range(N):
    S, P = input().split()
    list.append((S, int(P)))

name = "atcoder"
sum = 0

for i in range(N):
    sum += list[i][1]

for i in range(N):
    if list[i][1] > sum / 2:
        name = list[i][0]
    else:
        pass

print(name)
