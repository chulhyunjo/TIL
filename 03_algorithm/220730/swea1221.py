num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, int(input()) + 1):
    t, n = input().split()

    numbers = list(input().split())
    result = []
    print(f'#{tc}')
    for i in numbers:
        result.append(num.index(i))
    result.sort()
    for i in result:
        print(num[i], end = ' ')
    print()
