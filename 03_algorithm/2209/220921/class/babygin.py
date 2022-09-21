def babygin(s, n):
    global result
    if s == n:
        if num[0] == num[1] == num[2] and not (num[3]+num[4]+num[5])%3:
            result = 'Baby Gin'
        elif num[0] == num[1] == num[2] and num[3] == num[4] == num[5]:
            result = 'Baby Gin'
        elif not (num[0]+num[1]+num[2])%3 and num[3] == num[4] == num[5]:
            result = 'Baby Gin'
        elif not sum(num)%3:
            result = 'Baby Gin'
    else:
        for i in range(s,n):
            num[s], num[i] = num[i], num[s]
            babygin(s+1,n)
            num[s], num[i] = num[i], num[s]

for tc in range(1,int(input())+1):
    num = list(map(int,input()))
    result = 'Lose'
    babygin(0, 6)
    print(f'#{tc} {result}')
