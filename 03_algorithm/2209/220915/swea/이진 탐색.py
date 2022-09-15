def in_order(i):    # 왼쪽은 작은 값, 오른쪽은 큰값이므로 중위 순회로 하나씩 삽입
    global last
    if i <= N:      # 중위 순회
        in_order(2*i)           # 왼쪽 자식
        tree[i] = nums[last]    # 맨 아래 왼쪽 부터 왼->중->오 순으로 순서대로 삽입
        last += 1
        in_order(2*i+1)         # 오른쪽 자식


T = int(input())                # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())            # 노드의 개수
    tree = [0] * (N+1)          # 빈 트리 생성
    nums = list(range(1,N+1))   # 1~N까지의 수를 담기
    last = 0                    # 0번 인덱스부터 넣기 위한 변수
    in_order(1)                 # 중위 순회 시작
    print(f'#{tc} {tree[1]} {tree[N//2]}')