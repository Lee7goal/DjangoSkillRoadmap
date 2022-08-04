from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class AccountModel(AbstractUser):
    nick_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    wechat_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
