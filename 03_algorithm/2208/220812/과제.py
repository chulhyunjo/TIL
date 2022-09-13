t= int(input())
for _ in range(t):
    tc, n = input().split()
    n = int(n)
    arr = list(input().split())
    nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    new_arr =[0] * 10 # 숫자의 개수를 담을 리스트

    for num in arr: # 입력 받은 숫자 체계를 하나 씩 확인
        for i in range(10): # nums 배열이랑 확인
            if nums[i] == num:
               new_arr[i] += 1 # 같은 값이면 카운트

    print(f'{tc}')
    for i in range(10):
        for j in range(new_arr[i]):
            print(nums[i], end = ' ')
