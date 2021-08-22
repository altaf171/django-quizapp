from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.question_text




class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


# class Answer(models.Model):
#     question = models.OneToOneField(Question ,primary_key=True, on_delete=models.CASCADE)
#     answer = models.ForeignKey(
#         Choice, on_delete=models.CASCADE)
