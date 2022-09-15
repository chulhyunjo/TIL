def heap(i):        # 최소 힙 트리 만들기
    global last     # 마지막 인덱스
    last += 1       # + 1
    tree[last] = arr[i] # 현재 인덱스에 숫자리스트 순서대로 넣기
    c = last        # 현재 자식은 현재 인덱스
    p = c//2        # 부모는 현재 위치//2
    while p and tree[c] < tree[p]:  # 부모가 자식보다 클때 계속 실행
        tree[c], tree[p] = tree[p], tree[c] # 부모, 자식 바꾸기
        c = p       # 부모도 확인을 하기 위해 부모 위치로 변경
        p = c//2


T = int(input())    # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())    # N개의 노드
    arr = list(map(int,input().split()))    # 숫자 리스트
    tree = [0] * (N+1)  # 초기 트리 생성
    last = 0            # 인덱스 변수
    for i in range(N):
        heap(i)         # 최소 힙 만들기

    last_node = N       # 마지막 노드의 위치: N
    result = 0          # 조상들의 합을 담을 변수
    while last_node:    # 맨 위에까지 이동
        last_node //= 2 # 노드의 부모 위치
        result += tree[last_node]
    print(f'#{tc} {result}')