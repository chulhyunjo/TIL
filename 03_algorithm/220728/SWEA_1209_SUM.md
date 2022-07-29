# SWEA 1209. SUM

[출처]https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1#none



#### [문제 설명]

다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.

![image-20220728174811085](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20220728174811085.png)



#### [제약 사항]

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.



#### [입력]

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.



#### [출력]

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다.



#### [정답]

```python
for test in range(10):
    tc = int(input())

    array = [list(map(int, input().split())) for _ in range(100)]
	# 행 합
    col_max = 0
    for col in array:
        col_max = max(col_max, sum(col))
	
    # 열 합
    row_max = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += array[j][i]
        row_max = max(row_max, row_sum)
    
    # 대각선 합
    arrow_max = 0
    for i in range(100):
        arrow1_sum = 0
        arrow1_sum += array[i][i]
        arrow_max = max(arrow_max, arrow1_sum)
	# 대각선 합2
    for i in range(99,-1,-1):
        arrow2_sum = 0
        arrow2_sum += array[i][i]
        arrow_max = max(arrow_max, arrow2_sum)
    result_max = max(row_max, col_max, arrow_max)
    print(f'#{tc} {result_max}')
```



#### [문제 풀이]

- `array = [list(map(int, input().split())) for _ in range(100)]`

  - 2차원 배열 List를 담을 array를 선언한다.

- ```python
  # 행들의 합중 최대값을 0으로 선언
  col_max = 0
  # 행 합
  for col in array:
      # 현재까지 행들의 합중 최대값을 col_max에 초기화
      col_max = max(col_max, sum(col))
  ```

- ```python
      # 열들의 합중 최대값을 0으로 선언
      row_max = 0
      for i in range(100):
          row_sum = 0
          for j in range(100):
              # array[j][i]를 이용해서 열들의 합들을 row_sum에 대입
              row_sum += array[j][i]
          # 현재까지 행들의 합중 최대값을 col_max에 초기화
          row_max = max(row_max, row_sum)
  ```

  - `array[j][i]` 이용하기

- ```python
  # 대각선 합
  arrow_max = 0
  for i in range(100):
      arrow1_sum = 0
      # 대각선은 [0][0], [1][1], [2][2]..... [99][99] 인덱스
      arrow1_sum += array[i][i]
      arrow_max = max(arrow_max, arrow1_sum)
      # 대각선 합2
  for i in range(99,-1,-1):
      arrow2_sum = 0
      # 대각선은 [0][99], [1][98], [2][97]....[99][0] 인덱스
      arrow2_sum += array[99-i][i]
      arrow_max = max(arrow_max, arrow2_sum)
  ```
  
- 