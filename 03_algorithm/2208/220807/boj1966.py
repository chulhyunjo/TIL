from collections import deque
import sys

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    queue = deque(sys.stdin.readline().split())

    cnt = 0
    while True:
        if queue[0] == max(queue):
            x = queue.popleft()
            cnt += 1
            if m == 0:
                break
            m = m - 1
        else:
            queue.append(queue.popleft())
            if m: m -= 1
            else: m = len(queue) - 1

    print(cnt)