from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : '제목을 입력하세요.'
            },
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : '내용을 입력하세요.',
                'rows': 20,
            },
        )
    )
    class Meta:
        model = Article
        exclude =('user',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='댓글',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : '댓글을 작성하세요',
                'maxlength' : 200,
            }
        )
    )
    class Meta:
        model = Comment
        exclude = ('article','user',)