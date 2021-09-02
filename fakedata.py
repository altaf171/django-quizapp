import os
from faker import Faker
from random import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiztime2.settings')
import django
from quiz.models import Question
django.setup()


fake = Faker()

# fake.paragraph(nb_sentences=2, variable_nb_sentences=False)
# print(loremtext)


def create_question_set(no=1):
    for i in range(0, no):
        q_text = fake.sentence(nb_words=randint(5, 10))
        Question.objects.get_or_create(question_text=q_text)
        q = Question.objects.get(pk= i+1)
        answer_id = randint(0,3)  # random choice for answer
        for i in range(4):
            c_text = fake.sentence(nb_words=randint(2, 5))
            if i == answer_id:
                q.choices.create(choice_text=c_text, is_answer=True)  # add options
            else:
                q.choices.create(choice_text=c_text)  # add options

                

create_question_set(no=20)
