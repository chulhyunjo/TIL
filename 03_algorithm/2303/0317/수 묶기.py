import heapq

n = int(input())

minus = []
plus = []
one = 0

for _ in range(n):
    a = int(input())
    if a>1:
        heapq.heappush(plus, -a)
    elif a<=0:
        heapq.heappush(minus, a)
    else:
        one+=1

result = 0
for _ in range(len(minus)//2):
    a = heapq.heappop(minus)
    b = heapq.heappop(minus)
    result += a*b
for _ in range(len(plus)//2):
    a = heapq.heappop(plus)
    b = heapq.heappop(plus)
    result += a*b

if minus:
    result += minus[0]
if plus:
    result -= plus[0]
result += one

print(result)