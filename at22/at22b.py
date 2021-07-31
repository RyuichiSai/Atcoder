N = int(input())

cnt = 0
A_list = [0]*100001
for i in range(N):
    j = int(input())
    if A_list[j] == 1:
        cnt += 1
    else:
        pass
    A_list[j] = 1

print(cnt)
