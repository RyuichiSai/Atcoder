W = input()

ans = ""

for i in range(len(W)):
    if W[i] not in "aiueo":
        ans += W[i]
    else:
        pass

print(ans)
