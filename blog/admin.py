from django.contrib import admin
from django.contrib.admin import ModelAdmin
from blog.models import Article, Comment, Survey, Questions, Answers, Category

# Register your models here.


admin.site.register(Article)
admin.site.register(Comment)
