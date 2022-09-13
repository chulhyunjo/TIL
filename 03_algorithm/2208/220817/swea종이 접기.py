arr = [0] * 31
arr[1] = 1                          # 길이가 10인 사각형을 만들 수 있는 경우의 수 : 1
arr[2] = 3                          # 길이가 20인 사각형을 만들 수 있는 경우의 수 : 3
for i in range(3,31):               # 10<= N <= 300까지의 사각형을 만들수 있는 경우의 수 구하기
    arr[i] = arr[i-1] + 2 * arr[i-2]

for tc in range(1, int(input())+1):
    n = int(input())
    print(f'#{tc} {arr[n//10]}')