def dfs(i):
    if len(s) == m:
        print(*s)

    else:
        for j in range(len(arr)):
            if arr[j] in s: continue
            s.append(arr[j])
            dfs(i+1)
            s.pop()


n, m = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
s = []
dfs(0)