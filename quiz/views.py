from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .forms import NewUserForm
# Create your views here.


def starting_page(request):
    return render(request, 'quiz/index.html')


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('starting-page'))
    form = NewUserForm()
    return render(request, 'quiz/register.html', context={'form': form})
