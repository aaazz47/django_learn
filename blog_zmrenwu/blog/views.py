from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from comments.forms import CommentForm
from .models import Post, Category
# 为 BlogPostView 增加Markdown渲染
import markdown

class BlogIndexView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    

    def get_queryset(self):
        return Post.objects.all()[:5]


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 阅读量+1
    post.increase_views()
    # 评论
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }
    return render(request, 'blog/detail.html', context=context)

# class BlogPostView(generic.DetailView):
#     model = Post
#     template_name = 'blog/detail.html'


def archives(request, year, month):
    post_list = Post.objects.filter(
        pub_date__year = year,
        pub_date__month = month
    ).order_by('-pub_date')
    return render(request, 'blog/index.html', context={'post_list':post_list})

class ArchivesView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return Post.objects.filter(pub_date__year=year, pub_date__month=month)

# def category(request, name):
#     post_list = Post.objects.filter(
#         fen_lei__name = name
#     ).order_by('-pub_date')
#     return render(request, 'blog/index.html', context={'post_list':post_list})

class CategoryView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category, name=self.kwargs.get('name'))
        return Post.objects.filter(fen_lei=cate)
        # return super(CategoryView, self).get_queryset().filter(fen_lei=cate)
