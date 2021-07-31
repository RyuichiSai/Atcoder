S = input()
T = input()

for i in range(len(S)):

    if S[i] == T[i]:
        pass
    elif S[i] == "@" and T[i] == "@":
        pass
    elif S[i] == "@" and T[i] in {"a", "t", "c", "o", "d", "e", "r"}:
        pass
    elif T[i] == "@" and S[i] in {"a", "t", "c", "o", "d", "e", "r"}:
        pass
    else:
        print("You will lose")
        exit()

print("You can win")
