from django.contrib import admin

from .models import Question, Choice
from django.utils import timezone
import datetime

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
        (None, {"fields": ["question_txt"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
     inlines = [ChoiceInline]
     list_display = ["question_txt", "pub_date", "was_published_recently"]
     def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
     

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)