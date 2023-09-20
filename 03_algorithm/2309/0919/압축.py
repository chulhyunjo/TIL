w = input()
N = len(w)
stack = []
length = 0

cnt = 0
L = 0
num = 0
for i in range(N):
    if w[i] == '(':
        cnt += 1
    if w[i] != ')':
        stack.append(w[i])
    else:
        flag = 0
        while stack and flag == 0:
            x = stack.pop()
            if x == '(':
                flag = 1
            else:
                num += 1
        multi = int(stack.pop())
        cnt -= 1
        L = num * multi
        if not cnt:
            length += multi * num
            L = 0
            num = 0
        else:
            num = L

print(length + len(stack))