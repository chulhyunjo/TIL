for _ in range(int(input())):
    a, b = map(int,input().split())
    if a < b:
        a, b = b, a
    tmpa, tmpb = a, b
    while tmpb % tmpa != 0:
        tmpb, tmpa = tmpa, tmpb % tmpa

    print(a * b // tmpa)
