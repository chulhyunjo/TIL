import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

for t in range(int(input())):
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((a,s))

    visited = [False] * (n+1)
    times = [INF] * (n+1)
    times[c] = 0

    pq = []
    heapq.heappush(pq, (0,c))

    while pq:
        nowTime, now = heapq.heappop(pq)
        if visited[now]: continue
        visited[now] = True
        for next, nextTime in graph[now]:
            if nowTime+nextTime > times[next]: continue
            times[next] = min(times[next], nowTime+nextTime)
            heapq.heappush(pq, (times[next], next))

    answerCnt = 0
    answerTime = 0
    for i in range(1,n+1):
        if times[i] == INF: continue
        answerCnt += 1
        if answerTime < times[i]:
            answerTime = times[i]
    print(answerCnt, answerTime)