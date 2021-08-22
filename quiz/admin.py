from django.contrib import admin
from django.contrib.admin.decorators import register
# from django.contrib.auth.models import User
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)


# class UserAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'username':('firstname')}
