def sum1(i,s):
    global minV
    if i == n:
        minV = min(s, minV)
    elif s > minV:
        return
    else:
        for d in range(n):
            if not used[d]:
                used[d] = 1
                sum1(i+1, s+graph[i][d])
                used[d] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    used = [0] * n
    minV = 15*99
    sum1(0,0)
    print(f'#{tc} {minV}')