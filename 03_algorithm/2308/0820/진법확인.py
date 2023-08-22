def solution(expressions):
    use = []
    find = []
    can = [1] * 8

    def findcanUse(can):
        canUse = []
        for i in range(8):
            if can[i] == 1:
                canUse.append(i+2)
        return canUse

    for e in expressions:
        e = e.split()
        a, b, c = e[0], e[2], e[4]
        if c == 'X':
            find.append(' '.join(e))
            n = int(max(list(a) + list(b)))
            for i in range(2, n+1):
                can[i-2] = 0
        else:
            use.append(' '.join(e))
            n = int(max(list(a) + list(b) + list(c)))
            for i in range(2, n + 1):
                can[i - 2] = 0

    canUse = findcanUse(can)

    for u in use:
        u = u.split()
        a, b, c = u[0], u[2], u[4]
        for i in canUse:
            num1 = 0
            for j in range(len(a)):
                num1 += int(a[len(a)-j-1]) * (i**j)

            num2 = 0
            for j in range(len(b)):
                num2 += int(b[len(b) - j - 1]) * (i ** j)

            num3 = 0
            for j in range(len(c)):
                num1 += int(c[len(c) - j - 1]) * (i ** j)

            if u[1] == '+':
                if num1 + num2 != num3:
                    can[i-2] = 0
            elif u[1] == '-':
                if num1 - num2 != num3:
                    can[i-2] = 0

    canUse = findcanUse(can)
    answer = []
    for f in find:
        f = f.split()
        a, b = f[0], f[2]
        c = set()
        for i in canUse:
            num1 = 0
            for j in range(len(a)):
                num1 += int(a[len(a)-j-1]) * (i**j)

            num2 = 0
            for j in range(len(b)):
                num2 += int(b[len(b) - j - 1]) * (i ** j)

            if f[1] == '+':
                num3 = num1 + num2
            else:
                num3 = num1 - num2

            if num3 == 0:
                result = '0'
            else:
                result = ''
                while num3:
                    result = str(num3%i) + result
                    num3 //= i
                c.add(result)
                if len(c) > 1:
                    c = '?'
                    break
        if c == '?':
            answer.append(f'{f[0]} {f[1]} {f[2]} {f[3]} ?')
        else:
            c = list(c)
            answer.append(f'{f[0]} {f[1]} {f[2]} {f[3]} {c[0]}')
    return answer