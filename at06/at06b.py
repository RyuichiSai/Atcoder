N = int(input())

tri = [0]*N
tri[0:3] = [0, 0, 1]
for i in range(3, N):
    tri[i] = (tri[i-1] + tri[i-2] + tri[i-3]) % 10007
ans = tri[N-1]
print(ans)
