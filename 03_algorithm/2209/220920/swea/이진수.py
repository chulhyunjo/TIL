for tc in range(1, int(input())+1):
    n, num = input().split()
    n = int(n)
    result = 0
    for i in range(len(num)):
        if num[i].isdigit():
            result += int(num[i]) * 16**(n-1)
        else:
            result += (ord(num[i]) - 55) * 16 **(n-1)
        n -= 1
    ans = ''
    while result:
        ans = str(result%2) + ans
        result //= 2
    print(f"#{tc} {'0'+ans}")