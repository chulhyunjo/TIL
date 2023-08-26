import sys
input = sys.stdin.readline
N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()


for _ in range(M):
    m = int(input().strip())
    s = 0
    e = N-1
    answer = 0
    if nums[s] >= m or nums[e] <= m:
        print(0)
        continue
    while s <= e:
        mid = (s+e) // 2
        now = nums[mid]
        if now == m :
            answer = (N-mid-1) * mid
            break
        elif now > m:
            e = mid - 1
        elif now < m:
            s = mid + 1

    print(answer)

# nums_dict = dict()
# for i in range(1, N+1):
#     nums_dict[nums[i-1]] = i
#
# for _ in range(M):
#     m = int(f.readline().strip())
#     idx = nums_dict.get(m, -1)
#     if idx == -1:
#         print(0)
#     else:
#         answer = (N-idx) * (idx-1)
#         print(answer)
