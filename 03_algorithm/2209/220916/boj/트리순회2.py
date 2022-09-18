import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def inorder(i): # 중위 순회 돌기
    c1, c2 = tree.get(i)[0], tree.get(i)[1]
    if c1 != -1:
        inorder(c1)
    intree.append(i)
    if c2 != -1:
        inorder(c2)


def inorder_cnt(i): # 유사 중위 순회 돌기
    global cnt
    c1,c2 = tree.get(i) # 현재 노드의 자식 받아 오기
    if c1 != -1:  # 자식1이 있다면
        cnt += 1    # 이동+1
        inorder_cnt(c1)   # 자식1으로 이동
    if c2 != -1:  # 자식2가 있다면
        cnt += 1    # 이동 +1
        inorder_cnt(c2) # 자식2로 이동
    if i == intree[-1]: # 중위 순회의 마지막 노드에 도달하면
        print(cnt)      # 이동횟수 출력
        exit()          # 종료
    cnt += 1            # 돌아가는 이동 횟수 더하기

N = int(input().rstrip())   # 노드의 개수
tree = dict()               # 트리
root = 1                    # 루트 노드는 항상 1
for _ in range(N):          # 트리 만들기
    n, c1, c2 = map(int,input().rstrip().split())
    tree[n] = [c1,c2]
intree = []                 # 중위 순회 순서 담을 리스트
cnt = 0                     # 이동 횟수 담을 변수
inorder(1)
inorder_cnt(1)
