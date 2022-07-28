# SWEA 1208. Flatten

[출처](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=1208&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

#### [문제 설명]

한 쪽 벽면에 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 **최고점과 최저점의 간격을 줄이는 작업을 평탄화**라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 **작업을 한 후 최고점과 최저점의 차이**를 반환하는 프로그램을 작성하시오.



#### [제약 사항]

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

**주어진 덤프 횟수 이내에 평탄화가 완료되면** 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (**주어진 data에 따라 0 또는 1이 된다**).



#### [입력]

총 10개의 테스트 케이스가 주어지며, 각 테스트 케이스의 첫 번째 줄에는 덤프 횟수가 주어진다. 그리고 다음 줄에 각 상자의 높이값이 주어진다.



#### **[출력]**

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 최고점과 최저점의 높이 차를 출력한다.



#### [정답]

```python
for tc in range(1, 11):
    # 총 덤프(평탄화 작업) 횟수 입력
    n = int(input())
    # 상자 개수 리스트 생성
    array = list(map(int, input().split()))
    
    for i in range(n):
        # 제일 높게 쌓인 상자 더미의 위치를 찾는다
        max_idx = array.index(max(array))
        # 제일 낮게 쌓인 상자 더미의 위치를 찾는다
        min_idx = array.index(min(array))
        # 평탄화 작업이 완료되면 break
        if array[max_idx] - array[min_idx] <= 1:
            result = array[max_idx] - array[min_idx]
            break
        # 평탄화 작업 > 높은 곳에서 낮은 곳으로 1개를 옮긴다
        else:
            array[max_idx] -= 1
            array[min_idx] += 1
    # for 반복문이 완료되면 결과값을 얻는다
    else:
        result = max(array) - min(array)

    print(f'#{tc} {result}')
```



#### [문제 풀이]

평탄화를 시키기 위해서는 **가장 높게 쌓인 상자**를 가장 **낮게 쌓인 상자 더미**에 옮기는 작업을 반복해야한다.

```python
# 제일 높게 쌓인 상자 더미의 위치를 찾는다
max_idx = array.index(max(array))
# 제일 낮게 쌓인 상자 더미의 위치를 찾는다
min_idx = array.index(min(array))
```



- `if array[max_idx] - array[min_idx] <= 1:` 

  - 높게 쌓인 더미와 가장 낮은 더미의 차이가 1 이하일 경우 평탄화 완료

  - ```python
    array[max_idx] -= 1
    array[min_idx] += 1
    # 위의 조건에 맞지 않으면 평탄화 작업을 반복
    ```

- `result = max(array) - min(array)`
  - `break`가 선언 되지 않았을 때 `for~else` 문을 이용하여 마지막에 높이 차이를 결과값에 대입