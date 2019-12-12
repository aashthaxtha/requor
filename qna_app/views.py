from django.shortcuts import render,redirect
from .models import QuestionModel,CategoryModel
from .forms import QuestionForm
from django.http import HttpResponse
from .models import QuestionModel

# Create your views here.
def addques(req):
    # question=QuestionForm.objects.get()
    if req.method=="POST":
        form = QuestionForm(req.POST,req.FILES)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('Submitted')
            except:
                return HttpResponse('Failed')  

        else:    
            return HttpResponse(form.errors)

          

    else: 
        form=QuestionForm
        # question=QuestionModel.objects.all()
        return render(req,'questionmodel_create.htm',{'form':form})

def popular(req):
    question=QuestionModel.objects.filter(qn_votes__gt=2)
    return render(req,'question.html',{'question':question})

def question(req):
    question=QuestionModel.objects.all()
    return render(req,'questionmodel_list.html',{'question':question})


def update_question(req,id):
    # question = get_object_or_404(QuestionModel,id=id)
    question = QuestionModel.objects.get(id=id)
    if req.method=="POST":
        
        form=QuestionForm(req.POST,req.FILES,instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')  

        else:    
            return HttpResponse(form.errors)

    else:
        form=QuestionForm(instance=question)
        return render(req,'questionmodel_create.htm',{'form':form})

def delete(req,id):
    QuestionModel.objects.get(id=id).delete()
    return HttpResponse('deleted')



    
#get--only one object is returned
# filter-----to displays same title or id
# all----displays all