# 요청에 대한 인증(Authentication in Web requests)

- Django가 제공하는 인증 관련 built-in-forms 익히기



## Login

- 로그인은 **Session을 Create**하는 과정



> #### AuthenticationForm

- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력 받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증
- request를 첫번째 인자로 취함

```py
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            # 로그인 save X, login 함수
            auth_login(request, form.get_user()) # auth_login(request, 유저 정보)
            return redirect('arrticles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```



> login()

- `login(request, user, backend=None)`
- 인증된 사용자를 로그인 시키는 로직으로 view함수에서 사용됨
- 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용
- HttpRequest 객체와 User 객체가 필요



> get_user()

- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환



## Authenication with User

> 현재 로그인 되어있는 유저 정보 출력하기

- 템플릿에서 인증 관련 데이터를 출력하는 방법

```html
<div class="container">
    <h3>Hello, {{ user }}</h3>
    <a href="{% url 'accounts:login' %}">Login</a>
    <hr>
    {% block content %}
    {% endblock content %}
  </div>
```

> context processors

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
- 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것

- 현재 user 변수를 담당하는 프로세서는 `django.contrib.auth.context_processors.auth`

로그인 하지 않은 경우 `AnonymousUser`로 출력



