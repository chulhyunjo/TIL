def dfs(i, string, idx):
    if i == l:
        if check(string) >= 1 and (len(string) - check(string)) >= 2:
            print(''.join(string))
            return

    for j in range(c):
        if idx < j:
            if not visited[j]:
                visited[j] = True
                string.append(arr[j])
                dfs(i+1, string, j)
                visited[j] = False
                string.pop()


def check(string):
    count = 0
    for a in string:
        if a in ['a', 'e', 'i', 'o', 'u']:
            count+=1
    return count


l, c = map(int,input().split())
arr = sorted(list(input().split()))
visited = [False] * c
dfs(0,[],-1)
