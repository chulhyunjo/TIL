def dfs(idx,sum1,tar):
    global cnt

    if re and sum1 == tar:
        cnt += 1

    for j in range(n):
        if idx < j:
            if not visited[j]:
                visited[j] = True
                re.append(arr[j])
                dfs(j, sum1 + arr[j], tar)
                visited[j] = False
                re.pop()

                
re = []
n, s = map(int,input().split())
arr = list(map(int,input().split()))
visited = [False] * n
cnt = 0
dfs(-1,0,s)

print(cnt)