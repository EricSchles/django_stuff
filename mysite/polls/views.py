from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.conf.urls import url
from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(question,'polls/index.html',context)

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    return HttpResponse("You're looking at the results of question {}".format(response % question_id))

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$',detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
]
