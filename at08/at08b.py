import statistics

N = int(input())
S = [input() for i in range(N)]

a = statistics.mode(S)

print(a)
