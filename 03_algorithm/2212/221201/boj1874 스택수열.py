import sys
input = sys.stdin.readline

n = int(input().rstrip())
number = list(range(n,0,-1))
stack = []
result = []
answer = ''

for _ in range(n):
    result.append(int(input().rstrip()))
idx = 0
while number:
    answer += '+'
    stack.append(number.pop())
    while number and idx < n and stack and stack[-1] != result[idx]:
        answer += '+'
        stack.append(number.pop())
    while idx < n and stack and stack[-1] == result[idx]:
        answer += '-'
        stack.pop()
        idx += 1

if stack:
    print('NO')
else:
    for a in answer:
        print(a)