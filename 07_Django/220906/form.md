## django widget : form class에 이용

```py
class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATIONS_CHOICES = [
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
        ]
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices = NATIONS_CHOICES, widget=forms.RadioSelect)
```



1. form.as_p()
   - 각 필드가 단락(\<p>태그)으로 감싸져서 렌더링
2. as_ul()
   - 각 필드가 목록 항목\<li>태그으로 감싸져서 렌더링
   - \<ul> 태그는 직접 작성해야 함
3. as_table()
   - 각 필드가 목록 테이블(\<tr>태그)행으로 감싸져서 렌더링

- 특별한 상황이 아니라면 as_p()만 사용할 것





# ModelForm

```py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',) 제외 필드
        # 같이 사용 권장x
```





## 유효성 검증

```py
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:index', article.pk)
    return redirect('articles:new')
```

> is_valid()

- 유효한지 여부를 boolean으로 반환

  

> form.errors

- is_valid()에서 False값이 반환될때 form.errors에 값이 반환된다.





## UPDATE

1. request.POST
   - 사용자가 form을 통해 전송한 데이터
2. instance
   - 수정되는 대상

```py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```





## 데코레이터

> require_safe()

- require_GET이 있지만 Django에서는 require_safe()를 권장

- 405 Method Not Allowed
  - 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태



> require_http_methods()

- View 함수가 특정한 요청 method만 허용하도록하는 데코레이터

```py
@require_http_methods(['GET','POST'])
```



> require_POST()

- View 함수가 POST 요청 method만 허용하도록 하는 데코레이터

