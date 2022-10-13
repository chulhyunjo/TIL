def check(x, left, right):
    if x>n: return
    dp[abs(left-right)] = 1
    if visit[abs(left-right)][x] == 1: return
    else: visit[abs(left-right)][x] = 1
    if x<n:
        if left + weight[x] <= totalWeight:
            check(x+1, left+weight[x], right)
        if right + weight[x] <= totalWeight:
            check(x+1, left, right+weight[x])
        check(x+1, left, right)


n = int(input())
weight = list(map(int,input().split()))
ballN = int(input())
ball = list(map(int,input().split()))
totalWeight = sum(weight)

dp = [0] * (totalWeight+1)
visit = [[0] * (n+1) for _ in range(totalWeight+1)]
check(0, 0, 0)
for i in ball:
    if i > totalWeight:
        print('N', end=' ')
    elif dp[i] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')