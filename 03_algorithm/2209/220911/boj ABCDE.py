import sys
input = sys.stdin.readline

def dfs(x,cnt):
    global result
    if cnt == 4:                # 친구의 깊이가 4인 경우 result += 1
        result += 1
        return
    visited[x] = True
    for j in sorted(graph[x]):
        if not visited[j]:
            dfs(j,cnt+1)        # 백트래킹
            visited[j] = False
            if result:          # 친구의 깊이가 4인 경우를 이미 찾았을 때 return
                return

n, m = map(int,input().rstrip().split())    # N: 사람의 수, M: 관계의 수
graph = [[] for _ in range(n)]              # A->B의 관계를 담을 배열

for _ in range(m):                          # 관계 담기
    a, b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(n):
    visited = [False] * n
    cnt = 0
    dfs(i,cnt)
    if result:   # 결과가 이미 나왔으면 break
        break

if result:     # print(result)로 대체 가능
    print(1)
else:
    print(0)
