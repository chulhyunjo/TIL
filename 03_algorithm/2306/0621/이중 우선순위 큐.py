import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    min_pq = []
    max_pq = []
    cnt = 0
    visited = [False] * K
    for i in range(K):
        command, num = input().split()
        if command == 'I':
            heapq.heappush(min_pq, (int(num),i))
            heapq.heappush(max_pq, (-int(num),i))
            cnt += 1
            visited[i] = True
        if command == 'D':
            if not cnt: continue
            if num == '1':
                while max_pq and not visited[max_pq[0][1]]:
                    heapq.heappop(max_pq)
                if max_pq:
                    visited[max_pq[0][1]] = False
                    heapq.heappop(max_pq)
            else:
                while min_pq and not visited[min_pq[0][1]]:
                    heapq.heappop(min_pq)
                if min_pq:
                    visited[min_pq[0][1]] = False
                    heapq.heappop(min_pq)

            cnt -= 1
    min_num = max_num = 0
    while min_pq and not visited[min_pq[0][1]]:
        heapq.heappop(min_pq)

    while max_pq and not visited[max_pq[0][1]]:
        heapq.heappop(max_pq)

    if not cnt:
        print('EMPTY')
    else:
        print(-max_pq[0][0], min_pq[0][0])