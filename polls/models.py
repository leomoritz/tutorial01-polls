import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1)) # https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

"""ANOTAÇÕES
1. É importante adicionar __str__()métodos aos seus modelos, não apenas para sua própria conveniência ao lidar com o prompt interativo, 
mas também porque as representações dos objetos são usadas em todo o painel administrativo gerado automaticamente pelo Django.
"""