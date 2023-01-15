from collections import deque

N, L = map(int,input().split())
numbers = list(map(int,input().split()))
queue = deque()

# queue에는 numbers의 [숫자, 인덱스] 튜플 형식으로 삽입
for i in range(N): # 0~N-1
    # 숫자가 크면 pop
    while queue and queue[-1][0] > numbers[i]:
        queue.pop()
    # numbers 삽입
    queue.append((numbers[i], i))

    # 범위 벗어나면 삭제
    if queue[0][1] <= i-L:
        queue.popleft()

    print(queue[0][0], end=" ")