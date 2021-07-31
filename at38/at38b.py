H, W = map(int, input().split())
h, w = map(int, input().split())

if H == h or H == w or W == h or W == w:
    print("YES")
else:
    print("NO")
