from blog_system.common.models import BlogSystemSettings


def can_user_create_blog(user):
    settings = BlogSystemSettings.objects.first()

    return not user.is_authenticated or \
        user.blog_set.count() < settings.MAX_BLOGS_PER_USER
