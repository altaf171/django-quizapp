# Generated by Django 3.2.5 on 2021-08-20 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_choice_is_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
