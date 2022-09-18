from collections import deque

N, K = map(int,input().split()) # n: 수빈이의 위치, k: 동생의 위치
queue = deque()
queue.append((N,0))
v = [1] * 100001                # 방문 리스트
while True:
    n, cnt = queue.popleft()    # n 현재 탐색 위치, cnt: 이동 횟수
    if n == K:                  # 동생을 만났다면
        print(cnt)              # 이동 횟수 프린트
        exit()                  # 종료
    if n+1 <= 100000 and v[n+1]: # 한칸 앞으로 이동
        queue.append((n+1,cnt+1))
        v[n+1] = 0              # 방문 기록
    if 0 <= n-1 and v[n-1]:     # 뒤로 한칸 이동
        queue.append((n-1,cnt+1))
        v[n-1] = 0              # 방문 기록
    if 2*n <= 100000 and v[2*n]: # 2배로 순간이동
        queue.append((2*n,cnt+1))
        v[2*n] = 0