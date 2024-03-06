from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()

# class SlugifierMixin():
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
# Create your models here.
class Blog(models.Model):
    MAX_NAME_LENGTH = 30

    slug = models.SlugField(
        editable=False,
        unique=True,
    )
    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )
    description = models.TextField(
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)




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

