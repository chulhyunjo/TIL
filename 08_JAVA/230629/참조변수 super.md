### 참조변수 super

- 객체 자신을 가리키는 참조변수.
- 인스턴스 메서드(생성자)내에만 존재
- 조상의 멤버를 자신의 멤버와 구별할 때 사용



### super() - 조상의 생성자 - this()

- 조상의 생성자를 호출할 때 사용
- 조상의 멤버는 조상의 생성자를 호출해서 초기



```java
class Point3D extends Point {
    int z;
    Point3D(int x, int y, int z) {ㄴ
        //this.x = x;
        //this.y = y;
        super(x,y)
        this.z = z;
    }
}
```

- 생성자의 첫줄에 반드시 생성자를 호출해야한다.
- 그렇지 않으면 컴파일러가 생성자의 첫줄에 super()를 삽입