from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Choices
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
# Create your views here.

#check the except function
class DetailView(generic.DetailView):
    template_name="poll/details.html"
    model=Questions

class ResultView(generic.DetailView):
    template_name="poll/result.html"
    model=Questions

class IndexView(generic.ListView):
    template_name="poll/index.html"
    context_object_name="latest_questions"
    
    def get_queryset(self):
        return Questions.objects.order_by("publish_date")[:5]
    
    
def details(request,question_id):
    question=get_object_or_404(Questions,pk=question_id)
    return render(request,'pollapp/details.html',{'question' : question })
def results(request,question_id):
    question=get_object_or_404(Questions,pk=question_id)
    return render(request,"polls/results.html" ,{"question":question,})
def vote(request,question_id):
    question=get_object_or_404(Questions,pk=question_id)
    try:
        choice_selected=question.choices_set.get(pk=request.POST["choice"])
    except(KeyError,Choices.DoesNotExist):
        return render(request,'polls/details.html',{"question":question,"error_message":"You didn't select an option"})
    else:
        choice_selected.votes += 1
        choice_selected.save()
    return HttpResponseRedirect(reverse("poll:results", args=(question_id)))
def latest(request):
    latest_questions=Questions.objects.order_by('-publish_date')[:5]
    context={
        'latest_questions': latest_questions,
    }
    return render(request,'pollapp/index.html', context)