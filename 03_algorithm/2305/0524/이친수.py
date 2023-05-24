n = int(input())
if n == 1 or n == 2:
    print(1)
else:
    DP = [0] * (n+1)
    DP[1] = 1
    DP[2] = 1
    for i in range(2,n+1):
        DP[i] = DP[i-2] + DP[i-1]

    print(DP[n])