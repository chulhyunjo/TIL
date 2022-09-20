import sys
sys.stdin = open("sample_input.txt")
scan = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
       '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}
for tc in range(1, int(input())+1):
    n,m = map(int,input().split())
    graph = [input() for _ in range(n)]
    codes = set()
    result = set()
    for i in range(n):
        code = ''.join(graph[i]).strip('0')
        if code:
            codes.add(code)

    for code in codes:
        this_code = str(bin(int(code,16))).rstrip('0').lstrip('0b')
        length = 1
        while True:
            number = ''
            while len(this_code) < 56 * length:
                this_code = '0' + this_code
            check_code = this_code[-56*length:]
            for i in range(8):
                c_c = check_code[i*7*length:7*i*length+7*length:length]
                if scan.get(c_c,0):
                    number += scan.get(c_c)
                else:
                    break
            else:
                result.add(number)
                this_code = this_code[:len(this_code)-56*length].rstrip('0')
                length = 1
            if not len(number)==8 :length += 1

            if not this_code:
                length = 1
                break

    ans = 0
    for r in result:
        sum1 = 0
        add = 0
        for idx in range(8):
            if idx % 2:
                sum1 += int(r[idx])
            else:
                sum1 += int(r[idx]) * 3
            add += int(r[idx])
        if not sum1 % 10:
            ans += add
    print(f'#{tc} {ans}')