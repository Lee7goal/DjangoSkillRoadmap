from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account_manager.models import AccountModel

admin.site.register(AccountModel, UserAdmin)
