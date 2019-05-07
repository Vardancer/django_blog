from django.contrib import admin
from django.contrib.admin import ModelAdmin
import blog.models as bm

# Register your models here.


admin.site.register(bm.Article)
admin.site.register(bm.Comment)
admin.site.register(bm.Survey)
admin.site.register(bm.Questions)
admin.site.register(bm.Answers)
admin.site.register(bm.Response)


