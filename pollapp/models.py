from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_txt = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    # @admin.display(
    #     boolean=True,
    #     ordering="pub_date",
    #     description="Published recently?",
    # )
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
     
    def __str__(self):
        return self.question_txt
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True,related_name = "choices") # Why foreign key is used in the many side? 2. Table ma relations haru kasari maintain vako hunxa.  Visaulize garne
    choice_txt = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt
    