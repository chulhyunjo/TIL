from django import forms
from .models import Article

# 상속받을때는 첫 글자가 대문자여야 한다.(클래스)
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # form에는 TextField가 없다

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the Title',
                'maxlength' : 10,
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        )
    )


    class Meta:                 # 데이터 베이스와 Form을 연결 시켜주는 역할
        model = Article
        fields = '__all__'
        # exclude = ('title',) # 특정 필드만 제외하고 쓰고 싶을때 사용