from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):

        context = super(PostDetail, self).get_context_data()
        # categories라는 이름의 키에 모든 카테고리(Category.objects.all)를 가져와
        context['categories'] = Category.objects.all()
        # 카테고리가 지정되지 않은 포스트의 개수를 세라
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context

# ListView를 상속받은 PostList(p.326)
class PostList(ListView):
    # get_context_data 메서드는 ListView나 DetailView에 기본적으로 내장되어 있는 메서드
    # 단지 model = Post라고 선언하면 get_context_data에서 자동으로 post_list = Post.objects.all()을 명령
    # 그래서 post_list.html에서 {% for p in post_list %} 같은 명령어를 바로 활용할 수 있는 것!
    model = Post
    ordering = '-pk'

    # 원래는 내장 메서드인데 오버라이딩하겠다.
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        # categories라는 이름의 키에 모든 카테고리(Category.objects.all)를 가져와
        context['categories'] = Category.objects.all()
        # 카테고리가 지정되지 않은 포스트의 개수를 세라
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        { # post_list.html을 사용하기 때문에 PostList 클래스에서 context로 정의했던 부분을 딕셔너리 형태로 직접 정의해야 한다.
            'post_list': post_list,
            'category': category,
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'categories': Category.objects.all(),
        }
    )


