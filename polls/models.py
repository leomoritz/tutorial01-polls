import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField("Pergunta", max_length=200)
    pub_date = models.DateTimeField("Data de publicação")
    
    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
    
    def __str__(self):
        return self.question_text
    
    # https://docs.djangoproject.com/en/6.0/topics/i18n/timezones/
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Publicado recentemente?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    @admin.display(
        boolean=True,
        description="Tem opções?",
    )
    def has_choices(self):
        return self.choice_set.exists()
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Opção", max_length=200)
    votes = models.IntegerField("Voto", default=0)
    
    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"
    
    def __str__(self):
        return self.choice_text
    
    def has_votes(self):
        return self.votes > 0
    
    def has_question(self):
        return self.question is not None

"""ANOTAÇÕES
1. É importante adicionar __str__()métodos aos seus modelos, não apenas para sua própria conveniência ao lidar com o prompt interativo, 
mas também porque as representações dos objetos são usadas em todo o painel administrativo gerado automaticamente pelo Django"""