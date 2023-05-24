n = int(input())
if n == 1: print(0)
else:
    DP = [0] * (n+1)
    DP[1] = 0
    DP[2] = 1

    for i in range(3, n+1):
        DP[i] = (i-1) * (DP[i-1] + DP[i-2]) % 1000000000

    print(DP[n])
