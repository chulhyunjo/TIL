'''
5
6 9 5 7 4
'''

n = int(input())
arr = list(map(int,input().split()))
arr.reverse() # [4, 7, 5, 9, 6]

stack = [] # [(6, 1), (9,2), (5,3), (7,4), (4,5)]
result = [0] * n
for i in range(1, n):
    stack.append((arr.pop(), i))

    while stack and stack[-1][0] < arr[-1]:
        stack.pop()

    if stack:
        result[i] = stack[-1][1]
    else:
        result[i] = 0

print(*result)