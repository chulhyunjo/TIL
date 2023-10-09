num = list(input())
cnt = [0] * 2
for i in num:
    cnt[int(i)] += 1

c = 0
for i in range(len(num)):
    if num[i] == '1':
        num[i] = -1
        c += 1
        if c == cnt[1]//2:
            break
c = 0
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        num[i] = -1
        c += 1
        if c == cnt[0]//2:
            break

answer = ''
for i in range(len(num)):
    if num[i] != -1:
        answer += num[i]

print(answer)