import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def tree_search(pre,now):
    visited[now] = 0        # 현재 노드를 방문 기록
    for i in tree[now]:     # 이어지는 노드를 방문하기 위한 for문
        if visited[i]:      # 방문했는지 확인
            tree_search(now,i)  # 아래 -> 1번 노드로 이동해야 하므로 맨 아래로 깊숙히 탐색

    if animal[now][0] == 'W': # 현재 노드에 늑대가 있다면
        if result[now] - animal[now][1] < 0:    # 늑대가 현재 노드에 이동한 양의 개수보다 많다면
            result[pre] += 0                    # 다음 노드에 양이 이동하지 않는다
        else:
            result[pre] += result[now] - animal[now][1] # 현재 위치를 지나는 (양 - 늑대)가 다음 노드로 이동할 수 있다
    if animal[now][0] == 'S':   # 현재 노드에 양이 있다면
        result[pre] += result[now] + animal[now][1] # 다음 노드에 양의 마릿수 만큼 이동

N = int(input().rstrip())           # 노드의 수
tree = [[] for _ in range(N+1)]     # 트리 2중 리스트
animal = [('',0)] * (N+1)           # 현재 노드의 (양 or 늑대, 마릿수) 담을 리스트
for q in range(2,N+1):              # 2번 노드부터 입력
    A, num, p = input().rstrip().split()    # A: 양 or 늑대, num: 마릿수, p: 이어지는 노드 번호
    tree[q].append(int(p))          # 트리에 이어지는 노드를 담기
    tree[int(p)].append(q)          # 2
    animal[q]=(A,int(num))          # 위치별 양인지 늑대인지와 마릿수 저장
result = [0] * (N+1)                # 노드별 이동했을 때에 양의 마릿수를 담을 결과 리스트
visited = [1] * (N+1)               # 방문 리스트
tree_search(1,1)                    # 1번 루트 노드부터 탐색
print(result[1])