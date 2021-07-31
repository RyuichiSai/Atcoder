import math

N = int(input())
A = list(map(int, input().split()))

A = [i for i in A if not i == 0]

print(math.ceil(sum(A)/len(A)))
