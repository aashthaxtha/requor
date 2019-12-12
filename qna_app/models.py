from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    ctitle = models.CharField(max_length=255)
    cdesc = models.TextField(max_length=255)

    def __str__(self):
        return (self.cdesc) 
    

class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    qn_desc = models.TextField(max_length=255)
    qn_votes = models.IntegerField(default=0)
    qn_image = models.ImageField(upload_to='QuestionImage',blank=True,null=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    # objects=objects.models.Manager()------- greybox in object

    def __str__(self):
        return (self.qn_desc) 

      


class AnswerModel(models.Model):
    answered_by = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    ans_desc = models.TextField(max_length=255)
    ans_image = models.ImageField(upload_to='AnswerImage')
    is_accept = models.BooleanField()
    ans_votes = models.IntegerField(default=0)
    question = models.ForeignKey(QuestionModel,on_delete=models.CASCADE)

