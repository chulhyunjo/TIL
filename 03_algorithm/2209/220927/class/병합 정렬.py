def merge_sort(m):
    global cnt
    if len(m) == 1:
        return m
    mid = len(m) // 2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:len(m)])
    if left[-1] > right[-1] : cnt += 1
    return merge(left,right)

def merge(l,r):
    result = [0] * (len(l) + len(r))
    reIdx = lIdx = rIdx = 0
    while lIdx < len(l) or rIdx < len(r):
        if lIdx < len(l) and rIdx < len(r):
            if l[lIdx] <= r[rIdx]:
                result[reIdx] = l[lIdx]
                lIdx += 1
            else:
                result[reIdx] = r[rIdx]
                rIdx += 1
        elif lIdx < len(l):
            result[reIdx] = l[lIdx]
            lIdx += 1
        elif rIdx < len(r):
            result[reIdx] = r[rIdx]
            rIdx += 1
        reIdx += 1
    return result


for tc in range(1,int(input())+1):
    n = int(input())
    array = list(map(int,input().split()))
    cnt = 0
    ans = merge_sort(array)
    print(f'#{tc} {ans[n//2]} {cnt}')