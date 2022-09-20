for tc in range(int(input())):
    n = int(input())
    money = list(map(int,input().split()))
    total = int(input())
    dp = [0] * (total+1)
    dp[0] = 1
    for i in money:
        for j in range(1, total+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
    print(dp[total])
