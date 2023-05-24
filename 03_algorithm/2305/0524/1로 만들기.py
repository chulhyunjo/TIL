import sys
N = int(input())
INF = sys.maxsize
DP = [INF] * (N+1)
DP[N] = 0

while N > 1:
    DP[N-1] = DP[N] + 1
    if N % 2 == 0:
        DP[N//2] = min(DP[N//2], DP[N]+1)
    if N % 3 == 0:
        DP[N//3] = min(DP[N//3], DP[N]+1)
    N -= 1

print(DP[1])