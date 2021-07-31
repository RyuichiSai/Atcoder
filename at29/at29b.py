a = [input() for i in range(12)]
cnt = 0

for i in range(12):
    for j in range(len(a[i])):
        if a[i][j] == "r":
            cnt += 1
            break
        else:
            pass

print(cnt)
