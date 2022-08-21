n, m  = map(int, input().split())
arr = sorted(list(set(map(int,input().split()))))
s = []


def dfs(idx):
    if len(s) == m:
        print(*s)
        return
    else:
        for i in range(idx,len(arr)):
            s.append(arr[i])
            dfs(i)
            s.pop()


dfs(0)