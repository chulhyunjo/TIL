def dfs(pre, post, x):
    pre.add(x)
    post.add(graph[x])
    if graph[x] in pre:
        if pre == post:
            return pre.union(post)
        else:
            return set()
    else:
        return dfs(pre, post, graph[x])

N = int(input())
graph = [0] + [int(input()) for _ in range(N)]
answer = set()

for i in range(1, N+1):
    if i not in answer:
        answer.update(dfs(set(), set(), i))
print(len(answer))
print(*sorted(answer), sep='\n')