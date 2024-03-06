from django.db import models


class BlogSystemSettings(models.Model):
    MAX_BLOGS_PER_USER = models.IntegerField(
        default=3
    )

