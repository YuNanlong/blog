from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def post_list(request, category_slug=None, tag_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tag = None
        posts = Post.get_published().filter(category=category)
    elif tag_slug:
        category = None
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = Post.get_published().filter(tags__in=[tag])
    else:
        category = None
        tag = None
        posts = Post.get_published()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    return render(request, 'post/list.html', {'category': category, 'categories': categories, 'posts': posts, 'tag': tag})

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post.get_published(), publish__year=year, publish__month=month, publish__day=day, slug=post_slug)
    categories = Category.objects.all()
    return render(request, 'post/detail.html', {'categories': categories, 'post': post})

def post_pdf(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    html = render_to_string('post/post_pdf.html', {'post': post})                 
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"post_{}.pdf"'.format(post_id)
    weasyprint.HTML(string=html).write_pdf(response)
    return response
