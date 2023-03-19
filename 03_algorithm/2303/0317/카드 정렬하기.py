import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

result = 0
while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += a+b
    heapq.heappush(cards, a+b)

print(result)