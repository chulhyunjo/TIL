# SWEA 1206. View

### [문제 설명]

강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

아래와 같이 강변에 8채의 빌딩이 있을 때, 연두색으로 색칠된 여섯 세대에서는 좌우로 2칸 이상의 공백이 존재하므로 조망권이 확보된다. 따라서 답은 6이 된다.

![image-20220728163034363](C:\Users\chaom\AppData\Roaming\Typora\typora-user-images\image-20220728163034363.png)

A와 B로 표시된 세대의 경우는 왼쪽 조망은 2칸 이상 확보가 되었지만 오른쪽 조망은 한 칸 밖에 확보가 되지 않으므로 조망권을 확보하지 못하였다.

C의 경우는 반대로 오른쪽 조망은 2칸이 확보가 되었지만 왼쪽 조망이 한 칸 밖에 확보되지 않았다.



### [입력]

입력 파일의 첫 번째 줄에는 테스트케이스의 길이가 주어진다. 그 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트케이스가 주어진다.



### [출력]

\#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 조망권이 확보된 세대의 수를 출력한다.



### [정답]

```python
for tc in range(1, 11):
    n = int(input())
    array = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        if max(array[i-2 : i+3]) != array[i]:
            continue
        else:
            result += array[i] - sorted(array[i - 2:i + 3], reverse=True)[1]

    print(f'#{tc} {result}')
```



#### [문제 풀이]

문제가 길어서 상당히 복잡해 보이지만 간단한 문제였다.

현재 빌딩의 위치가 'i'라고 가정했을때 [ i - 2 ~ i + 2 ] 범위 안에서 가장 높은 빌딩이라면 조망권이 생긴다.



- `array = list(map(int, input().split()))`을 이용해서 빌딩들의 층 수를 나열한 리스트를 만든다.

- `if max(array[i-2 : i+3]) != array[i]: continue`
  - [ i - 2 : i + 2 ]의 범위에서 'i'번째 건물이 가장 높지 않으면 조망권이 생기지 않으므로 `continue`
- **가장 높다면 아래와 같이 실행**
  - `result += array[i] - sorted(array[i - 2:i + 3], reverse=True)[1]`
  - 총 층수를 담을 변수 `result`에 **현재 층수**에서 두 번째로 높은 빌딩의 높이를 뺀값을 구하여 result에 더한다.



`sorted(array[i - 2 : i + 3], reverse=True)[1]` 

:현재 범위에서 내림차순으로 나열한 후 2번째 값을 가져온다.

또한, `sorted(array[ i-2 : i + 3])[3]`으로 바꿀 수도 있다. 