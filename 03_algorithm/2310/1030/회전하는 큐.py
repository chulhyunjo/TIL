from collections import deque

N, M = map(int,input().split())
nums = list(map(int,input().split()))

queue = deque(list(range(1, N+1)))
answer = 0
for i in range(M):
    # 현재 칸이 원하는 숫자면 popleft만
    if queue[0] == nums[i]:
        queue.popleft()
        continue

    # 찾고자하는 숫자의 인덱스
    now_idx = queue.index(nums[i])
    # 왼쪽, 오른쪽으로 돌리는 최소의 방법 확인 후 회전
    if now_idx <= (N - i) - now_idx:
        answer += now_idx
        queue.rotate(-now_idx)
        queue.popleft()
    else:
        answer += (N - i) - now_idx
        queue.rotate((N - i) - now_idx)
        queue.popleft()

print(answer)