w = input()

w = sorted(w)

if len(w) % 2 == 1:
    print("No")
    exit()
else:
    pass

for i in range(len(w)):
    if i % 2 == 0:
        pass
    else:
        if w[i] == w[i - 1]:
            pass
        else:
            print("No")
            exit()

print("Yes")
