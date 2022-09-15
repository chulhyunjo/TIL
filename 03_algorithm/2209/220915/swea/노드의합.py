def post(i):            # 후위 순회
    if i <= N:
        post(2*i)       # 왼쪽 자식 탐색
        post(2*i+1)     # 오른쪽 자식 탐색
        if not tree[i]: # 비어있는 칸이면
            if 2*i+1 > N:   # 오른쪽 자식이 없으면
                tree[i] = tree[2*i] # 왼쪽 자식 그대로 가져온다
            else:
                tree[i] = tree[2*i] + tree[2*i+1]   # (왼쪽 + 오른쪽) 자식


T= int(input())         # 테스트 케이스
for tc in range(1, T+1):
    N, M, L = map(int,input().split())  # N: 노드의 수, M: 리프 노드의 수, L: 출력할 노드의 수
    tree = [0] * (N+1)                  # 트리 생성
    for _ in range(M):
        num, n = map(int,input().split())
        tree[num] = n                   # num: 노드 번호, n: 숫자
    post(1)                             # 루트부터 탐색
    print(f'#{tc} {tree[L]}')           # 출력