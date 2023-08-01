import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))
sums = [0] * (N+1)
sums[1] = nums[0]
for i in range(1,N):
    sums[i+1] =  sums[i] + nums[i]

for _ in range(M):
    a, b = map(int,input().split())
    print(sums[b] - sums[a-1])
