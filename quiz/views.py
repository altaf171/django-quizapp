from typing import List
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib import messages


from .forms import NewUserForm
from .models import Question
# Create your views here.


def starting_page(request):
    return render(request, 'quiz/index.html')

# def start_quiz(request):
#     question_list = Question.objects.order_by('id')
#     return render(request,'quiz/quizes.html' ,{'question_list':question_list})

class StartQuizView(View):
    def get(self, request, *args, **kwargs):
        if request.session.has_key('username'):
            username = request.session['username']
            question_list = Question.objects.order_by('id')
            return render(request,'quiz/quizes.html' ,{'question_list':question_list, 'username':username})
        else:
            return redirect('user-login-quiz')

    # def get(self,request,*args, **kwargs):
    #     form = QuizForm()

        # return render(request,'quiz/quizes.html' ,{'form':form})

    
    def post(self, request, *args, **kwargs):
        
        no_of_correct_answers = 0
        question_list = Question.objects.order_by('id')
        result_messages = {}

        for key,value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                question = get_object_or_404(Question,pk=int(key))
                choice =  question.choices.get(pk=int(value))
                print(question)
                print(choice.is_answer)

                if choice.is_answer :
                    no_of_correct_answers += 1
                    result_messages.update({key:'✔️'}) 
                else:
                    result_messages.update({key:'❌'}) 

                    
        
        print(result_messages)
        return render(request, 'quiz/quizes.html',{'result_messages':result_messages, 'correct_answers':no_of_correct_answers, 'question_list':question_list})


def user_login_for_quiz(request):
    if request.method == 'POST':
        if request.POST.__contains__('username'):
            username = request.POST['username']
            request.session['username'] = username
            request.session.set_expiry(864000) #10 days
            return redirect('start-quiz')

    #redirect to start quiz if session is allready set
    if request.session.has_key('username'):
        return redirect('start-quiz')

    
    return render(request, 'quiz/user-login.html')


def user_logout(request):
    if request.session.has_key('username'):
        try:
            del request.session['username']
        except: 
            print('error deleting user')
    
    return redirect('starting-page')




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