"""
입력(2<=N<=100,000 , 2<=K<=100,000)
25 5

출력
2
"""

N, K = map(int,input().split())
result = 0

# N이 K로 나눠지기위해 몇번 -1을 해야하는지
while True:
    nextNumber = (N//K) * K
    result += (N - nextNumber)
    N = nextNumber
    if N < K: break
    result += 1
    N //= K

result += (N - 1)
print(result)