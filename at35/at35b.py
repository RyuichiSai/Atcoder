S = input()
T = int(input())

x = y = 0
cnt = 0
ans = 0
list = [0]*4

for i in range(len(S)):
    if S[i] == "L":
        x -= 1
    elif S[i] == "R":
        x += 1
    elif S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1
    else:
        cnt += 1

if T == 1:
    print(abs(x) + abs(y) + cnt)
else:
    for i in range(cnt):
        ans = (abs(x) + abs(y))
        if ans == 0:
            ans += 1
        else:
            ans -= 1
    print(ans)
