# Form 데이터 전송

> HTML <form> element

-  데이터가 전송되는 방법을 정의
- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송**하는 역할을 담당
- 데이터를 어디(action)로 어떤 방식(method)으로 보낼지
- 핵심 속성
  - action
  - method



> ### action

- 입력 데이터가 전송될 URL을 지정
- 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐



> ### method

- 데이터를 어떻게 보낼 것인지 정의
- 입력 데이터의 HTTP request methods를 지정
- HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데 바로 GET 방식과 POST 방식



> HTML <input> element

- 사용자로부터 데이터를 입력 받기 위해 사용
- "type" 속성에 따라 동작 방식이 달라짐
  - input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용
  - 지정하지 않으면 기본: text
- 핵심 속성
  - name



> ### name

- form을 통해 데이터를 제출했을 때 name속성에 설정된 값을 서버로 전송
- 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
- 주요 용도는 GET / POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것
  - GET방식에서는 URL에서 `'?key=value&key=value/'` 형식으로 데이터를 전달

