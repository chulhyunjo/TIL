import sys
sys.setrecursionlimit(10**6)
def dfs(x,y,n):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit()
    if n == 1:
        cnt += 1
        return
    if not x <= r <= x+n and not y <= c <= y+n:
        cnt += n*n
        return
    n = n//2
    dfs(x,y,n)
    dfs(x, y+n, n)
    dfs(x+n,y,n)
    dfs(x+n,y+n,n)


N, r, c = map(int,input().split())
cnt = 0
dfs(0,0,2**N)