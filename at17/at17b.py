X = input()

X = X.replace("ch", "")
X = X.replace("o", "")
X = X.replace("k", "")
X = X.replace("u", "")

if not X:
    print("YES")
else:
    print("NO")
