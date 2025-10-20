N, M = map(int, input().split())

rates = []
for _ in range(N):
    rates.append(list(map(int,input().split())))

result = 0
use_Ids = []

for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            tmp = 0
            for l in range(N):
                tmp += max(rates[l][i], rates[l][j], rates[l][k])

            result = max(result, tmp)

print(result)