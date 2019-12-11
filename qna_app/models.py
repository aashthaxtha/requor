from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    qn_desc = models.TextField(max_length=255)
    qn_image = models.ImageField(upload_to='QuestionImage')


class AnswerModel(models.Model):
    answered_by = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    ans_desc = models.TextField(max_length=255)
    ans_image = models.ImageField(upload_to='AnswerImage')
    is_accept = models.BooleanField()
    votes = models.IntegerField()
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)



