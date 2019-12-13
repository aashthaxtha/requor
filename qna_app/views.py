from django.shortcuts import render,redirect
from .models import QuestionModel,CategoryModel,AnswerModel
from .forms import QuestionForm
from django.http import HttpResponse
from django.views.generic import CreateView,ListView


# Create your views here.
class QuestionModelCreateView(CreateView):
    model = QuestionModel
    fields='__all__'

class QuestionModelListView(ListView):
    model = QuestionModel
    queryset=QuestionModel.objects.all()

def question_detail(req,id):
    question=QuestionModel.objects.get(id=id)
    answer=AnswerModel.objects.filter(question=id)

    d={
        'question':question,
        'answer':answer
        }

    return render(req,'qna_app/detail.html',d)    
    # return render(req,'qna_app/detail.html',{'id':id})    
    


def addques(req):
    # question=QuestionForm.objects.get()
    if req.method == "POST":
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
        # form=QuestionForm(instance=question)
        category=CategoryModel.objects.all()
        return render(req,'questionmodel_create.htm',{'category':category})


def popular(req):
    question=QuestionModel.objects.filter(qn_votes__gt=2)
    return render(req,'question.html',{'question':question})

def question(req):
    if 'id' in req.session:

        question=QuestionModel.objects.all()
        return render(req,'questionmodel_list.html',{'question':question})
    else:
        return redirect('user:login')    


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
        category=CategoryModel.objects.all()
        return render(req,'questionmodel_create.htm',{'category':category})
        return render(req,'questionmodel_create.htm',{'form':form})
        
def delete(req,id):
    try:
        QuestionModel.objects.get(id=id).delete()
        return redirect('qna:read')

    except:
        return HttpResponse('Failed to delete,try again!')    

def upvote(req,id):
    instance = QuestionModel.objects.get(id=id)
    vote = instance.qn_votes+1
    instance.qn_votes=vote
    instance.save()
    return redirect('qna:read')

# def addans(req,id):
#     if req.method == "POST":
#         form = AnswerContent(req.POST,req.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return HttpResponse('Submitted')
#             except:
#                 return HttpResponse('Failed')  

#         else:    
#             return HttpResponse(form.errors)

          

#     else: 
#         # form=QuestionForm(instance=question)
#         category=CategoryModel.objects.all()
#         return render(req,'questionmodel_create.htm',{'category':category})

# def update_answer(req,id):


    
#get--only one object is returned
# filter-----to displays same title or id
# all----displays all

def test(req,id):
    question=QuestionModel.objects.get(id=id)
    answer=AnswerModel.objects.filter(question=id)
    return render(req,'test.html',{'question':question,'answer':answer})
    