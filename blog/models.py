from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    # 포스트 상세 페이지를 만들 때 URL이 도메인 뒤에 /blog/pk of record/를 쓰도록 했기 때문
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
