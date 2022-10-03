def findSet(x):
    while x != res[x]:
        x = res[x]
    return x

def union(x,y):
    res[findSet(y)] = findSet(x)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    res = [i for i in range(n+1)]

    for _ in range(m):
        a, b = map(int,input().split())
        union(a,b)

    result = 0
    for i in range(1, n+1):
        if res[i] == i:
            result += 1
    print(f'#{tc} {result}')