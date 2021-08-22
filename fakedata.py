from startquiz.models import Question
from faker import Faker
from random import *
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiztime.settings')
django.setup()


fake = Faker()

# fake.paragraph(nb_sentences=2, variable_nb_sentences=False)
# print(loremtext)


def create_question_set(no=1):
    for i in range(0, no):
        q_text = fake.sentence(nb_words=randint(5, 10))
        Question.objects.get_or_create(question_text=q_text)
        q = Question.objects.get(pk= i+1)
        for i in range(0, 4):
            c_text = fake.sentence(nb_words=randint(2, 5))
            q.choice_set.create(choice_text=c_text)  # add options
        c_list = q.choice_set.all()
        a_text = c_list[randint(0, 3)]  # random choice for answer
        q.answer_set.create(answer_text=a_text)
        # print(questions_record)
        # print(c_a)


create_question_set(no=4)
