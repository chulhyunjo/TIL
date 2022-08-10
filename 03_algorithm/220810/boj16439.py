n, m = map(int,input().split())
chicken = [list(map(int,input().split())) for _ in range(n)]

result = 0
for i in range(m):
    for j in range(m):
        if j != i:
            for k in range(m):
                if k != i and k != j:
                    sum1 = 0
                    for p in range(n-1):
                        sum1 = max(chicken[p][i], chicken[p+1][i])
                    sum2 = 0
                    for p in range(n-1):
                        sum2 = max(chicken[p][j], chicken[p+1][j])
                    sum3 = 0
                    for p in range(n-1):
                        sum3 = max(chicken[p][k], chicken[p + 1][k])
                    result = max(result, sum1 + sum2 + sum3)
print(result)