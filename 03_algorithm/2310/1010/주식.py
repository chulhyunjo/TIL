import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int,input().split()))
    max_num = nums.pop()
    answer = 0
    while nums:
        if nums[-1] <= max_num:
            answer += max_num - nums.pop()
        else:
            max_num = nums.pop()

    print(answer)