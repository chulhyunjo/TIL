scan = ['3211','2221','2122','1411','1132','1231','1114','1312','1213','3112']

for tc in range(1, int(input())+1):
    n, m = map(int,input().split())
    graph = [list(input()) for _ in range(n)]

    cords = set()
    for i in range(n):
        if graph[i].count('0') == m:
            continue
        pw = ''
        for j in range(m-1,-1,-1):
            if graph[i][j] != '0' and j != 0:
                pw = graph[i][j] + pw
            else:
                if pw:
                    cords.add(pw)
                pw = ''

    result = 0
    for cord in cords:
        now = ''
        for num in cord:
            if num.isnumeric():
                num = int(num)
            else:
                num = ord(num) - 55
            a = 15
            tmp = num
            code_2 = ''
            while a:
                code_2 = str(tmp%2) + code_2
                tmp //= 2
                a //= 2
            now += code_2
        now_code_cnt = len(now) // 56
        now = '0' * (4*now_code_cnt) + now
        for i in range(len(now)-1,-1,-1):
            if now[i] == '1':
                now = now[i-(56*(now_code_cnt)-1) if now_code_cnt >= 1 else i - 55 : i+1]
                break

        check_add = 0
        yes_code = 0
        for i in range(8):
            check = now[i*(7*now_code_cnt) : i*(7*now_code_cnt)+(7*now_code_cnt)]
            cnt = 1
            code_num = ''
            for j in range(len(check)):
                if j != len(check)-1 and check[j] == check[j+1]:
                    cnt += 1
                else:
                    code_num += str(cnt//now_code_cnt)
                    cnt = 1
            translate = scan.index(code_num)
            if i % 2:
                check_add += translate
            else:
                check_add += translate * 3
            yes_code += translate

        if not check_add % 10:
            result += yes_code

    print(f'#{tc} {result}')
