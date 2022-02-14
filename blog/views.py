from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') # private key, pk의 역순으로 정렬 -> 가장 최근에 만든 포스트부터 나열.

    return render(
        request,
        'blog/index.html',
        {
        'posts' : posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk = pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )