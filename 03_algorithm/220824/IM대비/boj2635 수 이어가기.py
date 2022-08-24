n = int(input())
cnt = 1
result = 0
result_l = []
while cnt <= n:
    temp = n
    temp2 = cnt
    lst = [n,cnt]
    i = 1
    while True:
        x = temp - temp2
        if x < 0:
            break
        lst.append(x)
        temp = lst[i]
        temp2 = lst[i+1]
        i += 1
    if result < len(lst):
        result = len(lst)
        result_l = lst
    cnt += 1

print(result)
print(*result_l)