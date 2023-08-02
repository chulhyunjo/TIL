import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int,input().split()))
S = [0] * N
C = [0] * M
S[0] = nums[0]
answer = 0

for i in range(1, N):
    S[i] = S[i-1] + nums[i]

for i in range(N):
    r = S[i] % M
    if r == 0:
        answer += 1
    C[r] += 1

for i in range(M):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)