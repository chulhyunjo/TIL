from collections import deque

N, K = map(int,input().split())
nums = list(map(int,input().split()))

# 확인한 리스트인지 담기
visited = dict()
queue = deque()

# 오름차순을 미리 담기
target = sorted(nums)

# 첫 리스트가 오름차순이면 0
if nums == target:
    print(0)
else:
    answer = -1
    queue.append((0, nums))
    # bfs로 완탐
    while queue:
        cnt, arr = queue.popleft()
        for i in range(N-K+1):
            # 배열 복사
            new_arr = arr[::]
            #뒤집기
            new = list(reversed(new_arr[i:i+K]))
            new_arr[i:i+K] = new
            # 확인한 리스트인지 확인
            if visited.get(str(new_arr) , 0): continue
            visited[str(new_arr)] = 1
            # 오름차순인지 확인
            if new_arr == target:
                answer = cnt+1
                break
            # 아니면 다음도 확인
            else:
                queue.append((cnt+1, new_arr))
        if answer != -1:
            break
    print(answer)
