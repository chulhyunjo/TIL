import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())        # 노드의 개수
tree_dict = dict()      # 부모의 자식을 담을 딕셔너리
result = [0] * (n+1)    # 각 노드의 부모를 담을 결과 리스트
visit = [0] * (n+1)     # 방문 리스트

for _ in range(n-1):
    a, b = map(int,input().split()) # a, b는 이어져 있다
    tree_dict[a] = tree_dict.get(a,[]) + [b]
    tree_dict[b] = tree_dict.get(b,[]) + [a]

def tree(now,par):
    result[now] = par   # 현재 노드의 부모를 담기
    visit[now] = 1      # 현재 노드 방문
    for ch in tree_dict[now]:   # 현재 노드와 이어져 있는 노드들 찾기
        if not visit[now]:      # 방문하지 않았다면
            tree(ch,now)        # 다음 노드로 들어가기, 현재 노드는 다음 노드의 부모
tree(1,1)               # 1번 노드 부터 시작
print(*result[2:], sep='\n')    # 2번 노드부터 차례대로 한 줄씩 출력