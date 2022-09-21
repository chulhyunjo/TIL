def check(ix, k, c):
    global maxV
    if c == 0:
        now = int(''.join(number))
        if now > maxV:
            maxV = now
    else:
        for i in range(ix,k-1):
            for j in range(i+1, k):
                number[i], number[j] = number[j], number[i]
                check(ix,k,c-1)
                number[i], number[j] = number[j], number[i]

for tc in range(1, int(input())+1):
    number, cnt = input().split()
    number = list(number)
    cnt = int(cnt)
    idx = maxV = 0
    while idx < len(number):
        check(idx, len(number), cnt)
        idx += 1
    print(f'#{tc} {maxV}')