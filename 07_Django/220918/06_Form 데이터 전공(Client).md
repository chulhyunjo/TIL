# Form 데이터 전공(Client)

> HTTP request methods

- HTTP
  - HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의

- HTTP Method예시
  - GET, POST, PUT, DELETE



> GET

- 서버로부터 정보를 조회하는데 사용
  - 즉, 서버에게 리소스를 요청하기 위해 사용
- 데이터를 가져올 때만 사용
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  - 데이터는 URL에 포함되어 서버로 보내짐



> Query String Parameters

- 사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
- 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성
- 기본 URL과 물음표(?)로 구분
  - `http://host:port/path?key=value&key=value`
- Query String이라고도 함



