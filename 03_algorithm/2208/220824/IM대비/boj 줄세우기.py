n = int(input())
people = list(range(n,0,-1))
nums = list(map(int,input().split()))
line = []
stack = []
for i in nums:
    for j in range(i):
        stack.append(line.pop())
    line.append(people.pop())
    while stack:
        line.append(stack.pop())

print(*line)