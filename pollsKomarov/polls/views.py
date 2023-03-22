from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Poll, Choice

def index(request):
    return render(request, "polls/index.html", {"latest_poll_list": Poll.objects.all()[:5]})

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "Вы ничего  не выбрали - ЭТО ХУЛИГАНСТВО!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
