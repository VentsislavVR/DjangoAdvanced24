from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Blog(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
    description = models.TextField(
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Post(models.Model):
    MAX_TITLE_LENGTH = 30
    title = models.CharField(
        max_length=MAX_TITLE_LENGTH
    )
    text = models.TextField(

    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Comment(models.Model):
    text = models.TextField(

    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

