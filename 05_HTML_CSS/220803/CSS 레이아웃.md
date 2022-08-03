# CSS 레이아웃

> 모든 요소는 **네모**이고 위에서 부터 아래로 쌓인다.



### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
- 요소가 Normal flow를 벗어나도록 함



#### 속성

- none: 기본값
- left
- right



## Flexbox

### CSS Flexible Box Layout

- 행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
  - cross axis(교차 축)
- 구성 요소
  - Flex Container(부모 요소)
  - Flex item(자식 요소)

- display : flex;

> flex는 item이 아닌 container에 적용시킨다.



- inline-flex : 테두리가 줄어든다



- 배치 설정
  - flex-direction
  - flex-wrap
- 공간나누기
  - justify-content(main axis)
  - align-content(cross axis)
- 정렬
  - aligin-items(모든 아이템을 cross axis 기준으로)
  - aligin-self(개별 아이템)





> 왜 써야하나?

이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position 뿐

너무 불편...

(수동 값 부여 없이)

1. 수직 정렬
2. 아이템의 너비와 혹은 간격을 동일하게 배치





### flex-direction

- Main axis 기준 방향 설정

- 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의

  - row:기본값 1, 2, 3

  - row-reverse 3, 2, 1 반대쪽으로

  - column : 아래로 1, 2, 3

  - column-reverse 3, 2, 1



### flex-wrap

- 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
- 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
  - wrap : 넘치면 그 다음 줄로 배치
  - nowrap : 한줄로 배치



### flex-flow

- flex-direction 과 flex-wrap 의 shorthand
- flex-flow: row nowrap;



### justify-content -> Main axis 기준

1. flex-start
2. flex-end
3. center
4. space-between
5. space-around
6. space-evenly



### aligin-content -> Cross axis 기준 

1. flex-start
2. flex-end
3. center
4. space-between
5. space-around
6. space-evenly