s = input()
ans = ""

if s[0] == "B":
    s.lstrip()
else:
    pass

n = len(s)

for i in range(n):
    if s[i] == "0":
        ans += "0"
    elif s[i] == "1":
        ans += "1"
    else:
        ans = ans[:-1]


print(ans)
