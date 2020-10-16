from django.contrib import admin
from .models import Profile, Question, Answer

# Register your models here.
admin.site.register(Profile)
# admin.site.register(Question)
admin.site.register(Answer)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'Name', 'No_of_Answer_Posted', 'Date')

    def Name(self, obj):
        return obj.profile.name

    def No_of_Answer_Posted(self, obj):
        return obj.answers.count()

    def Date(self, obj):
        return obj.created


admin.site.register(Question, QuestionAdmin)
