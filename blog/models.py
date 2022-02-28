from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Category(models.Model):
    # unique=True 기능은 동일한 name을 갖는 카테고리를 또 만들 수 없게 설정
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author field 생성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # null=True: 카테고리가 미분류된 포스트도 있을 수 있다
    # ForeignKey로 연결되어 있던 카테고리가 삭제됐다면 연결된 포스트까지 삭제되지 않고 해당 포스트의 category 필드만 null이 되도록
    # on_delete=models.SET_NULL로 설정
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    # 포스트 상세 페이지를 만들 때 URL이 도메인 뒤에 /blog/pk of record/를 쓰도록 했기 때문
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
