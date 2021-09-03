from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
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

    
    def post(self, request, *args, **kwargs):
        
        no_of_correct_answers = 0
        question_list = Question.objects.order_by('id')
        no_of_questions = question_list.count()
        result_messages = {k:' ' for k in range(1,no_of_questions)}
        print(result_messages)

        for key,value in request.POST.items():

            if key != 'csrfmiddlewaretoken':

                key = list(map(int,list(key.split(','))))  # split key for question id and question from forloop in template
                print('key 0 : ', key[0])
                print('key 1 : ', key[1])

                question = get_object_or_404(Question,pk=key[0])
                choice =  question.choices.get(pk=int(value))
                print(question)
                print(choice.is_answer)

                if choice.is_answer :
                    no_of_correct_answers += 1
                    result_messages.update({key[1]:'✔️'})  # key[1] question number from forloop in template
                else:
                    result_messages.update({key[1]:'❌'}) 

        print(result_messages)
        
        return render(request, 'quiz/quizes.html',{'result_messages':result_messages, 'correct_answers':no_of_correct_answers, 'question_list':question_list})

#login page
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

#logout function delete session data
def user_logout(request):
    if request.session.has_key('username'):
        try:
            del request.session['username']
        except: 
            print('error deleting user')
    
    return redirect('starting-page')
