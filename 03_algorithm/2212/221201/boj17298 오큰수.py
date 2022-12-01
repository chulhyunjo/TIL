n = int(input())
arr = list(map(int,input().split()))
stack = []
result = [-1]*n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
print(*result)