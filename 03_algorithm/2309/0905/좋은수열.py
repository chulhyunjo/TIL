N = int(input())

def check(num, l):
    num = num[::-1]
    for i in range(1, l//2+1):
        if num[:i] == num[i:i+i]:
            return False
    return True


def dfs(d, num):
    global flag
    if flag: return
    if d == N:
        flag = num
        return

    for i in '123':
        nxt = num + i
        if check(nxt, len(nxt)):
            dfs(d+1, nxt)

flag = 0
for n in '123':
    if not flag:
        dfs(1, n)

print(flag)