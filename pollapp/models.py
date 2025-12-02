from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_txt = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True,related_name = "choices") # Foreign key k ho? forward and reverse key relation.
    choice_txt = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_txt
    