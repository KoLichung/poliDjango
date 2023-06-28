from django.contrib import admin
from .models import User, QAPost


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')

@admin.register(QAPost)
class QAPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body')
