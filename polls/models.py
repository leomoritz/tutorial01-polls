import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    # https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def has_choices(self):
        return self.choice_set.exists()
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    def has_votes(self):
        return self.votes > 0
    
    def has_question(self):
        return self.question is not None

"""ANOTAÇÕES
1. É importante adicionar __str__()métodos aos seus modelos, não apenas para sua própria conveniência ao lidar com o prompt interativo, 
mas também porque as representações dos objetos são usadas em todo o painel administrativo gerado automaticamente pelo Django"""