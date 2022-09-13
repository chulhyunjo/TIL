'''
5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
#
# right = 0
# left = 0
#
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             left += arr[i][j]
#         elif i < j:
#             right += arr[i][j]
# print(left, right)
for i in range(n):
    for j in range(n):
        if i > j and i > n-1-j:
            print('*',end='')
        elif i < j and i < n-1-j:
            print('*', end='')
        elif i > j and i < n-1-j:
            print('*',end='')
        elif i < j and i > n-1-j:
            print('*',end='')
        else:
            print(' ',end='')
    print()
# arr = [['*'] * n for _ in range(n)]
# for i in range(n):
#     arr[i][i] = ' '
# for i in range(n):
#     arr[i][n-i-1] = ' '
#
# for i in arr:
#     print(''.join(i))
