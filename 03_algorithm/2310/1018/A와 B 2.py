def dfs(now, length):
    global flag
    if length == s:
        if now == S:
            flag = 1
        return
    if not flag:
        if now[-1] == 'A':
            dfs(now[:len(now)-1], length - 1)
        if now[0] == 'B':
            nxt = now[1:len(now)]
            dfs(nxt[::-1], length-1)

S = input()
s = len(S)
T = input()
t = len(T)

flag = 0
dfs(T, t)
print(flag)