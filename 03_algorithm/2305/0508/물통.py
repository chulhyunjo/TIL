import sys
sys.setrecursionlimit(10**5)
A, B, C = map(int,input().split())

water = [[0]*(B+1) for _ in range(A+1)]
answer = []
def dfs(a,b):
    water[a][b] = 1
    c = C-(a+b)
    if a == 0:
        answer.append(c)
    # C->A
    nxtA = c+a if c+a <= A else A
    if not water[nxtA][b]:
        dfs(nxtA, b)
    # A->C
    nxtA = 0 if c+a<=C else (c+a)-C
    if not water[nxtA][b]:
        dfs(nxtA, b)

    # C->B
    nxtB = c+b if c+b <= B else B
    if not water[a][nxtB]:
        dfs(a,nxtB)

    # B->C
    nxtB = 0 if c + b <= C else (c + b) - C
    if not water[a][nxtB]:
        dfs(a, nxtB)

    # A->B
    nxtA = 0 if a+b <= B else (a+b) - B
    nxtB = a+b if a+b <= B else B
    if not water[nxtA][nxtB]:
        dfs(nxtA, nxtB)

    # B->A
    nxtA = a + b if a + b <= A else A
    nxtB = 0 if a + b <= A else (a + b) - A
    if not water[nxtA][nxtB]:
        dfs(nxtA, nxtB)

dfs(0,0)
print(*sorted(answer))