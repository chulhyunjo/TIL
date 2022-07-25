for tc in range(1, int(input()) + 1):
    n = input()
    number = list(n)
    multi = 2
    print(f'#{tc}', end = ' ')
    while True:
        n_mul = int(n)
        n_mul *= multi
        if sorted(list(str(n_mul))) == sorted(number):
            print('possible')
            break
        if len(str(n_mul)) > len(number):
            print('impossible')
            break
        multi += 1