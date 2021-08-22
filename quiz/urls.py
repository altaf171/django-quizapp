from django.urls import path

from . import views

appname = 'quiz'

urlpatterns = [
    path('',views.starting_page,name='starting-page'),
    path('register',views.register_request,name='register')
]
