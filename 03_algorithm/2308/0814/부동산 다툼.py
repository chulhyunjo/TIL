import sys
input = sys.stdin.readline

# [1] 역순으로 탐색 ( x: 현재 노드, s: 막힌 부분)
def find(x, s):
    # 루트 노드 아닐 경우 2로 나눠서 부모 확인
    if x//2 > 1:
        # 막혀있다면 s = x//2
        if tree[x//2]:
            return find(x//2, x//2)
        # 아니면 부모 노드 탐색
        else:
            return find(x//2, s)
    else:
        # s가 막혀있다면 return s
        if tree[s]:
            return s
        # 아니라면 return 0
        else:
            return 0

N, Q = map(int,input().split())
tree = [0] * (N+1)

for _ in range(Q):
    n = int(input())
    x = find(n, n)
    # x == 0이면 땅을 점령할 수 있다.
    if not x:
        tree[n] = 1
    print(x)