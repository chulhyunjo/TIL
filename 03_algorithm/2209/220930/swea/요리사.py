def combination(x, y):
    if x == n//2:
        com.append(stack[:])
        return
    else:
        if y<n:
            stack.append(y)
            combination(x+1, y+1)
            stack.pop()
            combination(x,y+1)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    used = [0] * n
    com = []
    stack = []
    combination(0,0)

    minV = 100000
    for i in range(len(com)):
        notInCom = [j for j in range(n) if j not in com[i]]
        sum1 = 0
        for s1 in range(n//2):
            for s2 in range(n//2):
                sum1 += graph[com[i][s1]][com[i][s2]]
        for s3 in range(n//2):
            for s4 in range(n//2):
                sum1 -= graph[notInCom[s3]][notInCom[s4]]

        if abs(sum1)<minV:
            minV = abs(sum1)

    print(f'#{tc} {minV}')