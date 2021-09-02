from random import choices
from django.db.models import fields
from quiz.models import Question
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.base import Model
from django.forms.models import ModelForm


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# class QuizForm(ModelForm):
#     choices = Question.objects.
#     class Meta:
#         model = Question
#         fields = '__all__'
