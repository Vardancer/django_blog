from django.contrib import admin
from survey import models


class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('question',)}


admin.site.register(models.Questions, QuestionAdmin)
admin.site.register(models.Answers)
admin.site.register(models.Response)
admin.site.register(models.Survey)

