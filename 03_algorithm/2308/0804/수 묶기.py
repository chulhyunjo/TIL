import heapq
import sys
input = sys.stdin.readline

N = int(input())
minus = []
one = 0
plus = []

for _ in range(N):
    x = int(input())
    if x == 1:
        one += 1
    elif x > 1:
        heapq.heappush(plus, -x)
    elif x < 1:
        heapq.heappush(minus, x)

answer = 0
for _ in range(len(plus)//2):
    a = heapq.heappop(plus)
    b = heapq.heappop(plus)
    answer += a*b

for _ in range(len(minus)//2):
    b = heapq.heappop(minus)
    a = heapq.heappop(minus)
    answer += a * b

answer += one

if plus:
    answer -= plus[0]
if minus:
    answer += minus[0]
print(answer)