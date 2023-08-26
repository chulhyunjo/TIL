import sys
input = sys.stdin.readline
nums_dict = dict()

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
for i in range(1, N+1):
    nums_dict[nums[i-1]] = i

# for _ in range(M):
#     m = int(input())
for m in nums:
    idx = nums_dict.get(m, -1)
    if idx == -1:
        print(0)
    else:
        answer = (N-idx) * (idx-1)
        print(answer)
