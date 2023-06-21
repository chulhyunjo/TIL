from heapq import heappush, heappop
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M = int(input())
    numbers = []
    for i in range(M//10 + 1):
        numbers += list(map(int,input().split()))
    min_pq = []
    max_pq = []
    answer = []
    cnt = 0
    while cnt < M:
        if not cnt % 2:
            heappush(max_pq, -numbers[cnt])
        else:
            heappush(min_pq, numbers[cnt])
        cnt += 1

        while min_pq and -max_pq[0] > min_pq[0]:
            ma = -heappop(max_pq)
            mi = heappop(min_pq)
            heappush(max_pq, -mi)
            heappush(min_pq, ma)
        if cnt % 2:
            answer.append(-max_pq[0])
    print(len(answer))
    for i in range(len(answer)):
        tmp = 0
        print(answer[i], end=" ")
        if not (i + 1) % 10:
            print()
            tmp = 1
    if not tmp:
        print()