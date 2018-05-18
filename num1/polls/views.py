from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Intro
# Create your views here.
def index(request):
    intros = Intro.objects.all()
    context = {'intros':intros}
    return render(request, 'polls/index.html', context)

def main(request, name):
    intros = Intro.objects.all()
    if name == "main" :
        return render(request, 'polls/main.html')
    elif name == "login":
        return render(request, 'polls/login.html')
    elif name == "prediction":
        return render(request, 'polls/진단.html')
    elif name == "signin":
        return render(request, 'polls/회원가입.html')
    elif name == "reservation":
        return render(request, 'polls/reserve.html')
    else:
        return HttpResponse(name)
