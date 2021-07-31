a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(1)
elif a > b or a > c:
    print(2)
else:
    print(3)

if b > a and b > c:
    print(1)
elif b > a or b > c:
    print(2)
else:
    print(3)

if c > a and c > b:
    print(1)
elif c > a or c > b:
    print(2)
else:
    print(3)
