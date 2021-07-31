import sys

N = int(input())
S = input()
L = []

for i in range(N+1):

    if i == 0:
        L.append('b')
    elif i % 3 == 1:
        L.append('a' + L[-1] + 'c')
    elif i % 3 == 2:
        L.append('c' + L[-1] + 'a')
    elif i % 3 == 0:
        L.append('b' + L[-1] + 'b')
    else:
        pass

    if S == L[-1]:
        print(i)
        sys.exit()

print(-1)
