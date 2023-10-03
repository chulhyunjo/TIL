def spring():
    global answer
    new_trees = dict()
    for k, v in trees.items():
        x, y = k
        new =[]
        tmp = graph[x][y]
        for age in sorted(v):
            if tmp >= age:
                graph[x][y] -= age
                tmp -= age
                new.append(age + 1)
            else:
                # 여름
                graph[x][y] += age//2
                answer -= 1
        if new:
            new_trees[(x, y)] = new
    return new_trees


def autumn():
    global answer
    new_trees = dict()
    for k, v in trees.items():
        x, y = k
        cnt = 0
        for age in v:
            if age % 5 == 0:
                cnt += 1
        if cnt:
            new_trees[(x,y)] = cnt

    for k, v in new_trees.items():
        x, y = k
        for dx, dy in [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or N <= nx or N <= ny: continue
            trees[(nx, ny)] = trees.get((nx, ny), []) + ([1]*v)
            answer += v


def winter():
    for i in range(N):
        for j in range(N):
            graph[i][j] += A[i][j]

N, M, K = map(int,input().split())
graph = [[5]*N for _ in range(N)]
A = [list(map(int,input().split())) for _ in range(N)]
trees = dict()
answer = M

for _ in range(M):
    x, y, z = map(int,input().split())
    trees[(x-1, y-1)] = trees.get((x-1,y-1), []) + [z]

for _ in range(K):
    trees = spring()
    autumn()
    winter()

print(answer)