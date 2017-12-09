from django import template
from ..models import Post, Category


register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    """返回最近的5篇文章"""
    return Post.objects.order_by('-pub_date')[:num]

@register.simple_tag
def archives():
    """归档的标签"""
    return Post.objects.dates('pub_date', 'month', order='DESC')

@register.simple_tag
def categories():
    """分类的自定义标签"""
    return Category.objects.all()
