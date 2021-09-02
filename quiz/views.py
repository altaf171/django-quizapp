from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages

from .forms import NewUserForm
from .models import Question
# Create your views here.


def starting_page(request):
    return render(request, 'quiz/index.html')

def start_quiz(request):
    question_list = Question.objects.order_by('id')
    return render(request,'quiz/quizes.html' ,{'question_list':question_list})


# def quiz_detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'quiz/quiz-detail.html', {'question':question})


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created succesfully for ' + user)
            return redirect('login')
    form = NewUserForm()
    return render(request, 'quiz/register.html', context={'form': form})

def login_page(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request,username=username, password=password)
       if user is not None:
            login(request, user)
            return redirect('userpage')
    context = {}
    return render(request, 'quiz/login.html', context)

def userpage(request):
    return render(request, 'quiz/test.html')