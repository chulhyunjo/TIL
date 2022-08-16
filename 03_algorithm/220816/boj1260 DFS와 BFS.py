from collections import deque
dfs_arr = []
bfs_arr = []

def dfs(array,start,visit):
    dfs_arr.append(start)
    visit[start] = True
    for i in sorted(array[start]):
        if not visit[i]:
            dfs(array,i,visit)
    return dfs_arr


def bfs(array,start,visit):
    queue = deque([start])
    visit[start] = True
    while queue:
        x = queue.popleft()
        bfs_arr.append(x)
        for i in sorted(array[x]):
            if not visit[i]:
                visit[i] = True
                queue.append(i)
    return bfs_arr


n, m, v = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

print(*dfs(arr,v,visited_dfs))
print(*bfs(arr,v,visited_bfs))