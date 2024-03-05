from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()

class AccountsUserProxy(UserModel):
    class Meta:

        proxy = True
        ordering = ['username']
#
# print(UserModel.objects.all()) # order by pk
# print(AccountsUserProxy.objects.all()) # order by username


