N = int(input())

plans = []
for _ in range(N):
    s, e, p = map(int,input().split())
    plans.append((s,e,p))

plans.sort(key=lambda x: (x[1], x[2]))
dp = [(0,0,0)] * N
dp[0] = (plans[0])
for i in range(1, N):
    s, e, p = plans[i]
    pre_s, pre_e, pre_p = dp[i-1]
    if s >= pre_e:
        dp[i] = (s, e, p+pre_p)
    else:
        max_p = 0
        for j in range(i-1, -1, -1):
            s2, e2, p2 = dp[j]
            if s >= e2:
                max_p = max(p+p2, max_p)
        if max_p:
            dp[i] = (s, e, max_p)
        else:
            dp[i] = (s, e, p)
answer = 0
for i in range(N):
    answer = max(answer, dp[i][2])
print(answer)