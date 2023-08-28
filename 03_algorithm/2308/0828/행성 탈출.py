import sys
input = sys.stdin.readline

# 유니온 파인드
def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[b] = a
        return True
    return False


N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
parents = list(range(N))
nodes = []
for i in range(N):
    for j in range(i+1, N):
        nodes.append((graph[i][j], i, j))   # a->b, b->a 비용 C (nodes에 저장)
nodes.sort()    # 비용 오름차순으로 정렬
cnt = 0
result = 0

for c, a, b in nodes:
    if union(a,b):  # 비용 낮은 것 부터 연결
        cnt += 1
        result += c
        if cnt == N-1:  # N-1번 연결하면 끝
            break
print(result)