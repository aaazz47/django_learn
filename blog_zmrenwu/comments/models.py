from django.db import models

# Create your models here.

class Comment(models.Model):
    user_name = models.CharField('用户名', max_length=10)
    email = models.EmailField('邮箱', max_length=100)
    url = models.URLField('网址', blank=True)
    text = models.TextField('评论')
    created_time = models.TimeField('时间', auto_now_add=True)

    post = models.ForeignKey('blog.post', on_delete=models.CASCADE, verbose_name='所属文章')

    def __str__(self):
        return self.text[:20]
    