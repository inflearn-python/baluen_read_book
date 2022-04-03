from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()
    return render(request, 'blog/post_list.html', {
        'post_list': qs,
    })