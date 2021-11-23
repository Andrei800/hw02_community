from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Список групп'
    text = 'Информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
