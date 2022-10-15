from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Movie, Comment
from .forms import MovieForm, CommentForm

# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save(commit=False)
                movie.user_id = request.user
                movie.save()
                return redirect('movies:detail', movie.pk) # detail로 수정
            return redirect('movies:create')
        else:
            form = MovieForm()
    else:
        return redirect('accounts:login')
    context = {
        'form' : form
    }
    return render(request, 'movies/create.html', context)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.comments.all()
    comment_form = CommentForm()
    context = {
        'movie' : movie,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        if request.user == movie.user_id:
            if request.method == "POST":
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                    form.save()
                    return redirect('movies:detail', movie.pk)
                return redirect('movies:update', movie.pk)
            else:
                form = MovieForm(instance=movie)
        else:
            return redirect('movies:detail', movie.pk)
    else:
        return redirect('accounts:login')
    context = {
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if request.user == movie.user_id:
            movie.delete()
            return redirect('movies:index')
        else:
            return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

@require_POST
def comments_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie_id = movie
            comment.user_id = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user_id:
            comment.delete()
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')