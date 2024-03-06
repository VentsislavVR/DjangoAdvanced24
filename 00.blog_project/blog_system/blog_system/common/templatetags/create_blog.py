from django import template
from django.urls import reverse_lazy

from blog_system.common.utils import can_user_create_blog

register = template.Library()


@register.inclusion_tag('partials/create_blog.html')
def create_blog(user):
    return {
        'disabled': can_user_create_blog(user),
    }
