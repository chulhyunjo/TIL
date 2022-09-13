def search(target, start, end, cnt):
    middle = (start + end) // 2
    cnt += 1
    if target == middle:
        return cnt
    if target > middle:
        start = middle
    if target < middle:
        end = middle
    return search(target, start, end, cnt)

for tc in range(1, int(input())+1):
    page_start = 1
    page_end, a, b = map(int,input().split())

    a_cnt = search(a, page_start, page_end, 0)
    b_cnt = search(b, page_start, page_end, 0)

    if a_cnt < b_cnt:
        print(f'#{tc} A')
    if a_cnt > b_cnt:
        print(f'#{tc} B')
    if a_cnt == b_cnt:
        print(f'#{tc} 0')