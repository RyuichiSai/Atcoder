A, B, C = map(int, input().split())

if A + B == C and A - B == C:
    print("?")
elif A + B == C and not A - B == C:
    print("+")
elif not A + B == C and A - B == C:
    print("-")
else:
    print("!")
