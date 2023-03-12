import sys
input = sys.stdin.readline

nums = list(map(int,input().split()))

result = 'mix'
flag = 0
for i in range(7):
    if nums[i+1] - nums[i] == 1:
        if flag == -1:
            break
        flag = 1
    elif nums[i+1] - nums[i] == -1:
        if flag == 1:
            break
        flag = -1
    else:
        break
else:
    if flag == 1:
        result = 'ascending'
    elif flag == -1:
        result = 'descending'

print(result)