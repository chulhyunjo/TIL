n = int(input())
count = [0] * 1000001
arr = list(map(int,input().split()))

for i in range(n):
    count[arr[i]] += 1

stack = []
result = [-1] * n
for j in range(1,n):
    stack.append((arr.pop(), j))
    while stack and count[stack[-1][0]] <= count[arr[-1]]:
        stack.pop()

    if stack:
        result[j] = j  stack[-1][1]

print(*result)