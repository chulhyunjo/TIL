import sys
input = sys.stdin.readline


def dfs(i,idx):
    if i == 6:
        print(*result)

    for j in range(len(arr)):
        if idx < j:
            if not visited[j]:
                visited[j] = True
                result.append(arr[j])
                dfs(i+1,j)
                result.pop()
                visited[j] = False

i = 1
while i != 0:
    i, *arr = list(map(int,input().split()))
    result = []
    visited = [False] * len(arr)

    dfs(0,-1)
    print()