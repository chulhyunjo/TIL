for _ in range(int(input())):
    a, *a_card = map(int,input().split())
    b, *b_card = map(int,input().split())

    cnt_a = [0] * 5
    cnt_b = [0] * 5

    for i in range(a):
        cnt_a[a_card[i]] += 1
    for j in range(b):
        cnt_b[b_card[j]] += 1

    for q in range(4,0,-1):
        if cnt_a[q] > cnt_b[q]:
            print('A')
            break
        elif cnt_a[q] < cnt_b[q]:
            print('B')
            break
    else:
        print('D')
