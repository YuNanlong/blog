from django import template
from django.utils.safestring import mark_safe
import markdown
from ..models import Post

register = template.Library()

@register.filter(name="markdown")
def markdown_format(value):
    return mark_safe(markdown.markdown(value, extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ]))

@register.simple_tag(name="total_posts")
def total_posts(category=None):
    if category:
        return Post.get_published().filter(category=category).count()
    else:
        return Post.get_published().count()

@register.inclusion_tag('post/latest_posts.html')
def latest_posts():
    posts = Post.get_published().order_by('-publish')[:5]
    return {'posts': posts}

@register.inclusion_tag('post/similar_posts.html')
def similar_posts(post=None):
    if post:
        similar_posts = post.tags.similar_objects()[:5]
    else:
        similar_posts = None
    return {'similar_posts': similar_posts}
