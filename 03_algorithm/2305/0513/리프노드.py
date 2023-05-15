N = int(input())
parents = list(map(int,input().split()))
delete_num = int(input())

tree = [[] for _ in range(N)]
rootNum = 0
for i in range(N):
    if parents[i] == -1:
        rootNum = i
        continue
    tree[parents[i]].append(i)

answer = 0
def dfs(x, p):
    global answer
    if x == delete_num:
        if len(tree[p]) == 1: answer += 1
        return

    if not tree[x]:
        answer += 1
        return

    for next in tree[x]:
        dfs(next, x)

dfs(rootNum, rootNum)
print(answer)

