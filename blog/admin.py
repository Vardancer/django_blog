from django.contrib import admin
from django.contrib.admin import ModelAdmin
import survey.models as bm
import blog.models as bl

# Register your models here.


admin.site.register(bl.Article)
admin.site.register(bl.Comment)
admin.site.register(bm.Survey)
admin.site.register(bm.Questions)
admin.site.register(bm.Answers)
admin.site.register(bm.Response)


