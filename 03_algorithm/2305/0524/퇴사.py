N = int(input())
plan = [[0,0]]
for _ in range(N):
    plan.append(list(map(int,input().split())))

DP = [0] * (N+2)

for i in range(N, 0, -1):
    if plan[i][0] + i> N+1:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], DP[i+plan[i][0]] + plan[i][1])

print(DP[1])