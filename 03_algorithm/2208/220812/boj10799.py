laser = input()
cnt = 0
result = 0
for i in range(len(laser)-1):
    if laser[i] == '(':
        if laser[i+1] == '(':
            cnt += 1
        else:
            result += cnt

    else:
        if laser[i+1] == ')' and cnt > 0:
            cnt -= 1
            result += 1

print(result)