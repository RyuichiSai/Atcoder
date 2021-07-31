se = [map(int, input().split()) for _ in range(3)]
s, e = [list(i) for i in zip(*se)]
sum = 0

for i in range(3):
    sum = sum + (s[i] * (e[i]/10))

print(int(sum))
