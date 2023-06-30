### import 문

- 클래스를 사용할 때 패키지이름을 생략할 수 있다.

- 컴파일러에게 클래스가 속한 패키지를 알려준다.

  ```java
  import java.util.Date;
  
  class ImportTest{
      Date today = new Date();
  }
  ```

  

- java.lang패키지의 클래스는 import하지 않고도 사용할 수 있다.

  String, Object, System, Thread ...

- import 문을 선언하는 법

```java
import 패키지명.클래스명;
or
import 패키지명.*;
```

- import문은 컴파일 시에 처리되므로 프로그램의 성능에 영향없음
- 다음의 두 코드는 서로 의미가 다르다

```java
import java.util.*;
import java.text.*;    -> import java.*; // 다름
```

- 이름이 같은 클래스가 속한 두 패키지를 import할 때는 클래스 앞에 패키지 명을 붙여줘야한다.



### static import 문

- static 멤버를 사용할 때 클래스 이름을 생략할 수 있게 해준다.

  ```java
  import static java.lang.Integer.*;
  import static java.lang.Math.random;
  
  ```

  