from django.contrib import admin

# Register your models here.

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    classes = ["collapse"]

class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("DATA/HORA", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently", "has_choices"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    
admin.site.site_header = "Administração Enquetes"
admin.site.site_title = "Painel de Controle"
admin.site.index_title = "Bem-vindo ao painel administrativo de Enquetes"    

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
