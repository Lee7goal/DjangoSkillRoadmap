from django.contrib import admin
from .models import TodoModel


# Register your models here.

@admin.register(TodoModel)
class TodoAdmin(admin.ModelAdmin):
    pass
