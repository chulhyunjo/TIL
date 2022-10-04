def combination(depth, j,c):
    if c and depth <= n//2:
        if c not in coms:
            coms.append(c)
    elif depth> n//2:
        return
    if j <=n:
        combination(depth+1, j+1,c+[j])
        combination(depth, j+1, c)

def bfs(array):
    queue = []
    queue.append(array[0])
    visited = [0] * (n+1)
    visited[array[0]] = 1
    pop = 0
    while queue:
        x = queue.pop(0)
        pop += populations[x]
        for i in graph[x]:
            if not visited[i] and i in array:
                queue.append(i)
                visited[i] = 1
    return pop


n = int(input())
populations = [0] + list(map(int,input().split()))
city_pop = sum(populations)
graph = [[] for _ in range(n+1)]
for i in range(1,n+1):
    num, *arr = map(int,input().split())
    if num:
        for j in arr:
            graph[i].append(j)

coms = []
combination(0,1,[])
result = 10*100
for com in coms:
    not_com = [i for i in range(1,n+1) if i not in com]
    population = bfs(com)
    population2 = bfs(not_com)
    if population + population2 == city_pop:
        result = min(result, abs(population-population2))

if result != 1000:
    print(result)
else:
    print(-1)