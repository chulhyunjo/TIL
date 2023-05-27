def dfs(depth, nums, result):
    if nums == m:
        print(*result)
        return
    elif depth < n:
        dfs(depth+1, nums+1, result + [depth+1])
        dfs(depth+1, nums, result)

n, m = map(int,input().split())
numbers = list(range(1,n+1))
dfs(0,0,[])