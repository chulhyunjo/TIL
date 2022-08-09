for tc in range(1,11):
    d = int(input())
    box = list(map(int, input().split()))
    cnt = 0
    while cnt < d:
        for i in range(99, -1, -1):
            for j in range(i):
                if box[j] < box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]
        while box[0]>= box[1] and box[-1] <= box[-2]:
            box[0] -= 1
            box[-1] += 1
            cnt += 1
            if box[0] - box[-1] <= 1:
                break
            if cnt == d:
                break
        if box[0] - box[-1] <= 1:
            break

    for i in range(99, -1, -1):
        for j in range(i):
            if box[j] < box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]
    print(f'#{tc} {box[0]-box[-1]}')