from django.urls import path

from . import views

appname = 'quiz'

urlpatterns = [
    path('',views.starting_page,name='starting-page'),
    path('startquiz/',views.start_quiz,name='start-quiz'),
    # path('<int:question_id>/',views.quiz_detail,name='quiz-detail'),

    path('register',views.register_request,name='register'),
    path('login',views.login_page,name='login'),
    path('userpage',views.userpage,name='userpage')

]
