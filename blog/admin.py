from django.contrib import admin
from django.contrib.admin import ModelAdmin
import blog.models as bl

# Register your models here.


admin.site.register(bl.Article)
admin.site.register(bl.Comment)

