from django import template
from blog.models import Post
from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.simple_tag
def most_comments_posts(count = 3):
    # создаёт перменную count_coments хранящию количество коментариев у каждого из постов и потом бы убираем те посты у кого нет ни 1 комента и по убыванию количества коментов
    return Post.objects.annotate(count_coments=Count("coments")).exclude(count_coments=0).order_by("-count_coments")[:count]


@register.filter(name='markdown')
def mark_downformat(text):
    return mark_safe(markdown.markdown(text))   