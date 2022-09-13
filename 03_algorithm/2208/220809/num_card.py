T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = int(input())
    counts = [0] * 11 # 숫자 개수를 담을 리스트 선언

    for i in range(n):  # 숫자 하나 씩 확인해서 리스트에 담기
        counts[numbers % 10] += 1
        numbers //= 10

    maxV = counts[0] # 가장 큰 값이 나온 개수 담을 변수 선언
    max_num = 0 # 가장 큰 숫자 담을 변수 선언

    for i in range(11):
        if counts[i] >= maxV: # 개수가 현재 가장 큰 값보다 클 경우, 같으면 숫자가 큰 값이 나와야 되므로 >=
            maxV = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {maxV}')