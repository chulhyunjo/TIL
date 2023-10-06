from collections import deque
import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    command = deque(list(input().rstrip()))
    p = int(input())
    nums = deque(input().lstrip('[').rstrip(']\n').split(','))
    if nums[0] == '':
        nums = []

    cnt = 0
    answer = ''
    while command:
        while command and command[0] == 'R':
            cnt += 1
            command.popleft()

        while command and command[-1] == 'D':
            if nums:
                if cnt % 2:
                    nums.pop()
                else:
                    nums.popleft()
                command.pop()
            else:
                answer = 'error'
                break

        if answer: break

    if answer:
        print(answer)
        continue
    if cnt%2:
        nums.reverse()
    print('['+','.join(nums)+']')