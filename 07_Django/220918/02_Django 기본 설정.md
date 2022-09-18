# Django 기본 설정

> Django 4.0릴리즈로 인해 3.2(**LTS**) 버전을 설치

- $pip install django==3.2.13



> 패키지 목록 생성

- $pip freeze > requirements.txt



> ## LTS

- Long Term Support (장기 지원 버전)
- 일반적인 경우보다 장기간에 걸쳐 지원하도록 고아된 소프트웨어 버전
- 배포자는 LTS 확정을 통해 장기적이고 안정적인 지원을 보장함



> 프로젝트 생정

- $django-admin startproject project .
  - ' . '을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성하게 된다.



> 서버 실행

- python manage.py runserver





## 프로젝트 구조

- \__init__.py
  - python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
  - 별도로 추가 코드 작성 X
- asgi.py
  - Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정 X
- settings.py
  - Django 프로젝트 설정을 관리
- urls.py
  - 사이트의 url과 적절한 views의 연결을 지정
- wsgi.py
  - Web Server Gateway Interface
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포 시에 사용하며 지금은 수정 X
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용 하는 커매드라인 유틸리티



## 어플리케이션(앱)

> 애플리케이션 생성

$ python manage.py startapp [appname]



> #### 애플리케이션 구조

- admin.py
  - 관리자용 페이지를 설정하는 곳
- apps.py
  - 앱의 정보가 작성된 곳
  - 별도로 추가 코드 작성x
- models.py
  - 앱에서 사용하는 Model작성
  - MTV의 M
- tests.py
  - 프로젝트의 테스트 코드를 작성
- views.py
  - view 함수들이 정의 되는 곳
  - MTV 패턴의 V에 해달



> 애플리케이션 등록

- 프로젝트에서 앱을 사용하기 위해서 반드시 프로젝트의 `settings.py`의 `INSTALLED_APPS`에 추가해야함



> 주의사항

- 반드시 생성후 등록
  - 먼저 등록하고 생성할려면 생성되지 않음