N, A, B = map(int, input().split())
sd = []
for i in range(N):
    s, d = input().split()
    sd.append((s, int(d)))

ans = 0
for i in range(N):
    if sd[i][1] >= A and sd[i][1] <= B:
        if sd[i][0] == "East":
            ans += sd[i][1]
        else:
            ans -= sd[i][1]
    elif sd[i][1] < A:
        if sd[i][0] == "East":
            ans += A
        else:
            ans -= A
    else:
        if sd[i][0] == "East":
            ans += B
        else:
            ans -= B

if ans < 0:
    print("West", abs(ans))
elif ans == 0:
    print(0)
else:
    print("East", ans)
