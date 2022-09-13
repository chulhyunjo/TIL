for tc in range(1,int(input())+1):
    n = int(input())
    arr = list(map(int,input().split())) + [0]

    result = 0
    result2 = 0
    max_cnt = 0
    cnt = 1
    for i in range(1,n+1):
        if arr[i] > arr[i-1]:
            cnt += 1

        elif cnt > 1 and arr[i] <= arr[i-1]:
            result += 1
            if cnt > max_cnt:
                result2 = sum(arr[i-cnt:i])
            max_cnt = max(max_cnt, cnt)
            if cnt == max_cnt:
                result2 = max(result2, sum(arr[i-cnt:i]))
            cnt = 1
    print(f'#{tc} {result} {result2}')