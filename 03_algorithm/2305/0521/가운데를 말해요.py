import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap1 = []
heap2 = []
for i in range(n):
    num = int(input())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, -num)
    else:
        heapq.heappush(heap2, num)

    if heap2 and heap2[0] < -heap1[0]:
        l = heapq.heappop(heap1)
        r = heapq.heappop(heap2)

        heapq.heappush(heap1, -r)
        heapq.heappush(heap2, -l)
    print(-heap1[0])

