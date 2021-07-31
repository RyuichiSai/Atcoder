A = input() + "A"
B = input() + "B"
C = input() + "C"

N = len(A) + len(B) + len(C)
s = A[0]

for i in range(N):
    if s == "a":
        s = A[0]
        A = A[1:]
    elif s == "b":
        s = B[0]
        B = B[1:]
    elif s == "c":
        s = C[0]
        C = C[1:]
    elif s == "A":
        print("A")
        exit()
    elif s == "B":
        print("B")
        exit()
    elif s == "C":
        print("C")
        exit()
