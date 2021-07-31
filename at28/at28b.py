S = input()
L = [0]*6

for i in range(len(S)):
    if S[i] == "A":
        L[0] += 1
    elif S[i] == "B":
        L[1] += 1
    elif S[i] == "C":
        L[2] += 1
    elif S[i] == "D":
        L[3] += 1
    elif S[i] == "E":
        L[4] += 1
    elif S[i] == "F":
        L[5] += 1

print(*L)
