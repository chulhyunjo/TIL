numbers = input().split('-')
stack = []
for i in numbers:
    if '+' in i:
        plus = i.split('+')
        sum1 = 0
        for i in plus:
            sum1 += int(i)
        stack.append(sum1)
    else:
        stack.append(i)
result = int(stack[0])
for i in range(1,len(stack)):
    result -= int(stack[i])
print(result)