from django.urls import path

from . import views

appname = 'quiz'

urlpatterns = [
    path('',views.starting_page,name='starting-page'),
    # path('startquiz/',views.start_quiz,name='start-quiz'),
    path('startquiz/',views.StartQuizView.as_view(),name='start-quiz'),
    # path('<int:question_id>/',views.quiz_detail,name='quiz-detail'),

    path('userlogin/',views.user_login_for_quiz,name='user-login-quiz'),
    path('logout/',views.user_logout,name='logout'),

    path('register',views.register_request,name='register'),
    path('login',views.login_page,name='login'),
    path('userpage',views.userpage,name='userpage')

]


