from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            return redirect('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form': form
    }

    return render(request, 'articles/sign.html', context)


@login_required
def index(request):
    context = {
        'articles': Article.objects.filter(user=request.user),
    }

    return render(request, 'articles/index.html', context)


@login_required
def detail(request, pk):
    context = {
        'article': Article.objects.get(id=pk),
    }

    return render(request, 'articles/detail.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            return redirect('articles:detail', pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form
    }

    return render(request, 'articles/sign.html', context)


@login_required
def delete(request, pk):
    Article.objects.get(id=pk).delete()

    return redirect('articles:index')


@login_required
def duplicate(request, pk):
    article = Article.objects.get(id=pk)
    new = Article.objects.create(
        user=article.user,
        price=article.price,
        memo=article.memo
    )

    new.save()

    return redirect('articles:index')