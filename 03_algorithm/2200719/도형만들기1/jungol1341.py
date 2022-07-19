s, e = map(int, input().split())

if s<=e:
    for i in range(s, e+1):
        for j in range(1,10,3):
            print(f'{i} * {j} = {i*j:2d}', end = '   ')
            print(f'{i} * {j+1} = {i*(j+1):2d}', end = '   ')
            print(f'{i} * {j+2} = {i*(j+2):2d}')
        print()
else:
    for i in range(s, e-1, -1):
        for j in range(1,10,3):
            print(f'{i} * {j} = {i*j:2d}', end = '   ')
            print(f'{i} * {j+1} = {i*(j+1):2d}', end = '   ')
            print(f'{i} * {j+2} = {i*(j+2):2d}')
        print()