from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
UserModel = get_user_model()
class Profile(models.Model):
    MAX_NAME_LENGTH = 30
    display_name = models.CharField(max_length=MAX_NAME_LENGTH)

    USER = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

