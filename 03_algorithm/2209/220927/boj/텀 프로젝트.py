import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i):
    global result
    visited[i] = 1
    team.append(i)
    if visited[arr[i]]:
        if arr[i] in team:
            result += team[team.index(arr[i]):]
        return
    else:
        dfs(arr[i])

for tc in range(int(input())):
    n = int(input().rstrip())
    arr = [0] + list(map(int,input().rstrip().split()))
    visited = [0] * (n+1)
    result = []
    for k in range(1,n+1):
        if not visited[k]:
            team = []
            dfs(k)
    print(n-len(result))