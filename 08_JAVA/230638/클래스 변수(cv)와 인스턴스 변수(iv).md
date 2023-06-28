# 클래스 변수(cv)와 인스턴스 변수(iv)

인스턴스 변수 - 개별 속성

클래스 변수 - 공통 속성



```java
Class Card {
    // 개별 속성(iv)
    String kind;	// 무늬
    int number;		// 숫자
    
    // 공통 속성(cv)
    static int width = 100;	//폭
    static int height = 250;//높이
}

Card c = new Card();
// iv는 객체이름.변수
c.kind = "HEART";
c.number = 5;
// cv는 클래스이름.변수
Card.width = 200;
Card.height = 300;
```

