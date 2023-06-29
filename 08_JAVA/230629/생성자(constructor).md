## 생성자(constructor)

- 인스턴스가 생성될 때마다 호출되는 **'인스턴스 초기화 메서드'**

- 인스턴스 생성시 수행할 작업(iv 초기화)에 사용
- 이름이 클래스 이름과 같다
- 리턴값이 없다(void 안붙임)
- 모든 클래스는 반드시 생성자를 가져야 한다



```java
class Card { //클래스 이름: Card
    Card() { //매개변수 없는 생성자
        // 인스턴스 초기화 작업
        
    }
    //오버로딩
    Card(String kind, int number) { // 매개변수 있는 생성자
        // 인스턴스 초기화 작업
    }
    
}
Card c = new Card(); //-> 생성자 호출
```



### 기본 생성자(default contructor)

- 매개변수가 없는 생성자 (클래스이름(){})
- 생성자가 하나도 없을 때만, 컴파일러가 자동 추가



### 생성자 this()

- 생성자에서 다른 생성자 호출할 때 사용
- 다른 생성자 호출시 첫 줄에서만 사용가능
- 코드의 중복을 제거함.

```java
class Car2{
    String color;
    String gearType;
    int door;
    
    Car2(){
        this("white", "auto", 4);
    }
    
    Car2(String color){
        this(color, "auto", 4);
    }
    
    Car2(String color, String gearType, int door) {
        this.color = color;
        this.gearType = gearType;
        this.door = door;
    }
}
```



### 참조변수 this

- 인스턴스 자신을 가리키는 참조변수
- 인스턴스 메서드(생성자 포함)에서 사용가능
- 지역변수(lv)와 인스턴스 변수(iv)를 구별할 때 사용

- 인스턴스메서드에 지역변수로 숨겨진 채로 존재한다.



