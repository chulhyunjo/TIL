# SSR, CSR 차이

> SSR (Server Side Rendering)

말 그래도 서버에서 그린다



- template을 보면 html안에 파이썬으로 되어있다. 브라우저는 해당 파이썬을 이해할 능력이 없다.
- URL로 요청을 받으면 -> urls 타고 views에서 render를 진행
- render하는 시점에서 파이썬으로 되어있는 html을 그냥 html로 변환해서 리턴
- 자바의 경우는 JSP를 읽을수 없으니까 서버에서 읽어서 html로 만들어서 리턴
- 팔로우 누르면 창이 위로 올라간다, 클릭-> 새로 html을 그려서 주기 때문에



> CSR (Client Side Rendering)

말그래도 클라이언트에서 그린다.

- 자바스크립트에 비동기 통신
- REST API 형식
- 특징이 서버에서 HTML을 그려주지 않는다
- 대신 JSON형태를 리턴 (TMDB requests)
- HTML이 아니라 json만 리턴
- 얘를 그리기위해 또 다른 html이 필요(Vue, React...)
- 서버가 두가지로 변화 (분업이 가능)