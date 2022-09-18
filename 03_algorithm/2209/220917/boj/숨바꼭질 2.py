from collections import deque

N, K = map(int,input().split())
queue = deque()
queue.append((N,0))
result = 0                          # 최소 시간에 동생을 찾을 경우의 수
result_time = int(1e5)              # 동생을 찾는데 최소로 걸린 시간을 담을 변수
v = [1] * 100001                    # 방문 리스트
while queue:
    n, cnt = queue.popleft()        # n: 현재 위치, cnt: 시간
    v[n] = 0                        # 방문 기록을 밖에 빼는 이유
                                    # 최소 시간에 동생을 찾을 경우의 수를 담아야 하므로 동생위치는 최소 시간때 방문 기록 처리해야함
    if cnt > result_time:           # 최소 시간이 지나면 break
        break
    if n == K:                      # 동생을 찾으면
        result += 1                 # result += 1
        result_time = cnt           # 최소 시간 = cnt
    if n+1 <= 100000 and v[n+1]:    # 앞으로 한칸
        queue.append((n+1,cnt+1))
    if 0 <= n-1 and v[n-1]:         # 뒤로 한칸
        queue.append((n-1,cnt+1))
    if 2*n <= 100000 and v[2*n]:    # 순간이동
        queue.append((2*n,cnt+1))
print(result_time, result, sep='\n')