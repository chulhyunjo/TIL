def dfs(v):
    visited[v] = True
    stack.append(v)
    for i in arrList[v]:
        if not visited[i]:
            dfs(i)

arrList = [[],
           [2,3],
           [4,5],
           [1,7],
           [2,6],
           [2,6],
           [4,5,7],
           [3,6]]
visited = [False] * 8
stack = []
dfs(1)
stack = map(str,stack)
print('-'.join(stack))