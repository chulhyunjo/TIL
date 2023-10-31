import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# 루트노드 1번부터 거리 저장하면서 탐색
def find(now):
    for nx, d in tree[now]:
        if not visited[nx]:
            visited[nx] = 1
            answer[nx] = answer[now] + d
            find(nx)


N = int(input())
tree = [[] for _ in range(N+1)]

# 노드 연결
for _ in range(N-1):
    a, b, c = map(int,input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

# 방문체크
visited = [0] * (N+1)
# 거리
answer = [0] *(N+1)
visited[1] = 1

find(1)
print(max(answer))