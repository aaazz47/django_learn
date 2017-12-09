from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.html import strip_tags

class Category(models.Model):
    name = models.CharField('分类', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('标题',max_length=40)
    pub_date = models.DateTimeField('发布时间')
    update_time = models.DateTimeField('更新时间')
    content = models.TextField('内容')
    description = models.TextField('描述', blank=True, max_length=100)
    tag = models.ManyToManyField(Tag, blank=True)
    fen_lei = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    views = models.PositiveIntegerField('阅读量', default=0)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.description:
            # 跳过 Markdonw 渲染
            self.description = strip_tags(self.content)[:54]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = "博文"
        ordering = ['-pub_date']
