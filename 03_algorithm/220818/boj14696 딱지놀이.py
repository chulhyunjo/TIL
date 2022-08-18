n = int(input())
for _ in range(n):
    a, *arr_a = map(int,input().split())
    b, *arr_b = map(int,input().split())

    a_count = [0] * 5
    b_count = [0] * 5
    for i in arr_a:
        a_count[i] += 1
    for j in arr_b:
        b_count[j] += 1

    for i in range(4, 0, -1):
        if a_count[i] > b_count[i]:
            print('A')
            break
        elif a_count[i] < b_count[i]:
            print('B')
            break
    else:
        print('D')