import datetime
from email.policy import default

from django.db import models
from django.forms import IntegerField
from django.utils import timezone



class Question(models.Model):
  question_text = models.CharField(max_length=250)
  pub_date = models.DateTimeField("Data published")

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return timezone.now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=250)
  votes = models.IntegerField(default=0)

  def __str__(self) -> str:
    return self.choice_text