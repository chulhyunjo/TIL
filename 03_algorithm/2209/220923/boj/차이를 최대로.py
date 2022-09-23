def per(p,cnt,pre):
    global maxV
    if p == n:
        maxV = cnt if maxV < cnt else maxV
    else:
        for i in range(n):
            if not used[i]:
                used[i] = 1
                if p!=0:
                    per(p+1, cnt + abs(nums[pre]-nums[i]), i)
                else:
                    per(p+1, cnt, i)
                used[i] = 0


n = int(input())
nums = list(map(int,input().split()))
maxV= -(100*8)
used = [0] * n

per(0,0,0)
print(maxV)