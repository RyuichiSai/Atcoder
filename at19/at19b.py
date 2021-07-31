
s = input()

ans = s[0]
cnt = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cnt += 1
    else:
        ans += str(cnt) + s[i]
        cnt = 1
ans += str(cnt)
print(ans)
