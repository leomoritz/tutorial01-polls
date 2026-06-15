from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect

# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Choice, Question

# Create your views here.


"""Nas partes anteriores deste tutorial, os templates tem sido fornecidos com um contexto que contém as variáveis question e latest_question_list. 
Para a DetailView a variavel question é fornecida automaticamente – já que estamos usando um modelo Django (Question), Django é capaz de determinar 
um nome apropriado para a variável de contexto. Contudo, para ListView, a variável de contexto gerada automaticamente é question_list.
Para sobrescrever nós fornecemos o atributo context_object_name, especificando que queremos usar latest_question_list no lugar. 
Como uma abordagem alternativa, você poderia mudar seus templates para casar o novo padrão das variáveis de contexto – 
mas é muito fácil dizer para o Django usar a variável que você quer."""


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now() #lte = less than or equal to
        ).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST["choice"] retorna o ID da opção selecionada, como uma string. Os valores de request.POST são sempre strings.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):  # caso uma choice não seja selecionada
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1  # Evita condições de corrida
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
