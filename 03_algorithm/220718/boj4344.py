for tc in range(int(input())):
    lst = list(map(int, input().split()))
    summ = 0
    result = []
    for i in lst[1:]:
        summ += i
    avg = summ / lst[0]
    for i in lst[1:]:
        if i > avg:
            result.append(i)
    print(f'{len(result)/lst[0] * 100:.3f}%')

