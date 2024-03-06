def can_user_create_blog(user):
    return not user.is_authenticated or user.blog_set.count() <= 3
