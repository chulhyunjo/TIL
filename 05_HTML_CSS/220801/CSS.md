## CSS

> 스타일을 저장하기 위한 언어
>
> Cascading Style Sheets

```CSS
h1 {
    color : blue;
    font-size: 15px;
}
```

- CSS구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성(Property): 어떤 스타일 기능을 변경할지 결정
  - 값(Value): 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인(inline)
  - 인라인을 쓰게 되면 실수가 잦아짐(중복도 있을 것이고, 찾기가 어렵다)
- 내부 참조(embedding) - `<stlye>`
  - 내부 참조를 쓰게 되면 코드가 너무 길어짐
- 외부 참조(link file)- 분리된 CSS 파일
  - 가장 많이 쓰는 방식



### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS

- computed : 해당 요소에 최종 계산된 CSS



#### 선택자(Selector) 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마친표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디 선택자
  - (#) 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



### CSS 적용 우선순위(Cascading order)

> 범위가 좁을수록 강하다.

- CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.
  - 중요도 - 사용시 주의
    - !important
  - 우선순위(Specificity)
    - 인라인>id>class, 속성, pseudo-class>요소, pseudo-element
  - CSS 파일 로딩 순서

class = green, blue일 경우 > css 밑에 있는 요소의 색으로 변함





### 상속

- 부모요소의 속성을 자식에게 상속
  - 속성중에는 상속 되지 않는 것도 있다
  - 되는것
    - Text관련(font, color, text-align), opacity, visibility
  - 안되는것
    - 여백, 레이아웃x



### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용

- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - 브라우저의 기본글자 기준 (16px)



> 크기 단위(viewpoint)

- 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- **vw**, vh, vmin, vmax

- **px**는 브라우저의 크기를 변경해도 그대로
- **vw**는 브라우저의 크게에 따라 크기가 변함



### 색상 단위

- 색상 키워드(background-color: red;)
  - 대소문자 구분x
  - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(color : rgb(0,255,0);)
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현
  - '#' +  16진수 표기법
- HSL 색상(color : hsl(0, 100%, 50%);)
  - 색상, 채도, 명도를 통해 특정 색을 표현
- a는 alpha(투명도)



## 결합자

- **자손 결합자(공백)**
  - selectorA 하위의 **모든** selectorB 요소
- **자식 결합자(>)**
  - selectorA **바로 아래**의 selectorB 요소
  - h1>p>span x, h1>span o
- 일반 형제 결합자(~)
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
- 인접 형제 결합자(+)
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택



## Box model

- 모등 HTML요소는 box 형태로 되어 있다.

- 하나의 박스는 네부분으로 이루어짐

  - margin
    - 테두리 바깥의 외부 여백 배경색을 지정x
  - border
    - 테두리 영역
  - padding
    - 테두리 안쪽의 내부 여백 
    - 요소에 적용된 배경색
    - 이미지는 padding까지 적용
  - content
    - 글이나 이미지 등 요소의 실제 내용

  **134페이지**



```css
.border{
    border: 2px dashed black;
}

.border{
    border-width : 2px;
    border-style : dashed;
    border-color : black;
}
```



### CSS 원칙 2

- display에 따라 크기와 배치가 달라진다.



> 대펴적으로 활용되는 display

- display : block
  - 줄바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어감
- display: inline
  - 줄 바꿈 x
  - content 너비 만큼 가로 폭을 차지
  - width, height, margin-top,margin-bottom 지정 x
  - 상하 여백은 line-height로 지정



- 블록: div/ ul, ol, li/ p/ hr/ form 등
- 인라인 : span/ a/ img/ input, label/ b,em,i,strong 등



### CSS position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치 될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative : 상대 위치
    - 원래 위치로 갈려면?
    - 원래위치는 투명 > 사람눈에만 이동
  - absolute : 절대 위치
    - static이 아닌 요소를 찾고(position:realtive) 이동
    - 없는 경우 브라우저 기준
    - normal flow에서 벗어난다 (167pg)
  - fixed : 고정위치
    - viewport 기준으로 이동
  - sticky: 스크롤에 따라 static -> fixed로 변경



