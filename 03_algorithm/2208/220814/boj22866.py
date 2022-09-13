import copy

n = int(input())
arr = list(map(int, input().split()))
arr2 = copy.copy(arr)
stack = []
result = [0] * n
for i in range(1, n):
    stack.append((arr.pop(), i))

    while stack and arr and stack[-1][0] <= arr[-1]:
        stack.pop()

    if stack:
        result[i] += len(stack)
print(result)

stack = []
for i in range(n-1,1,-1):
    stack.append((arr2.pop(), i))

    while stack and arr and stack[-1][0] <= arr[-1]:
        stack.pop()

    if stack:
        result[i] += len(stack)

print(result)
