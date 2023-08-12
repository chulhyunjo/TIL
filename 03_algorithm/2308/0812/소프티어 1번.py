import time
start = time.time()
nums_dict = dict()

# N, M = map(int,input().split())
# nums = list(map(int,input().split()))

N = 50000; M = 2000000
nums = list(range(10, 50000*10+1, 10))
Q = list(range(10000, 10000*200000+1, 10000))

nums.sort()
for i in range(1, N+1):
    nums_dict[nums[i-1]] = i

# for _ in range(M):
#     m = int(input())
for m in Q:
    idx = nums_dict.get(m, -1)
    if idx == -1:
        print(0)
    else:
        answer = (N-idx) * (idx-1)
        print(answer)
print(time.time() - start)