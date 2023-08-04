N = input().split('-')
stack = []
for i in N:
    M = i.split('+')
    sum1 = 0
    for j in M:
        sum1 += int(j)
    stack.append(sum1)

result = stack[0]
for i in range(1, len(stack)):
    result -= stack[i]

print(result)
