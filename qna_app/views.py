from django.shortcuts import render
from .models import QuestionModel

# Create your views here.
def addques(req):
    question=QuestionModel.objects.all()
    return render(req,'newques.html',{'question':question})

    
#get--only one object is returned
# filter-----to displays same title or id
# all----displays all