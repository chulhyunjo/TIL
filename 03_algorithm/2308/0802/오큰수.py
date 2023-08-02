N = int(input())
numbers = list(map(int, input().split()))
answer = [-1]
stack = [numbers.pop()]

for i in range(N-1):
    while stack and stack[-1] <= numbers[-1]:
        stack.pop()
    if not stack:
        answer.append(-1)
    else:
        answer.append(stack[-1])

    stack.append(numbers.pop())

print(*reversed(answer), sep=' ')