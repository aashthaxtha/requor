from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse

# Create your views here.
 
def loginauth(req): 
    if req.method=="POST":
        e = req.POST.get('email')
        p = req.POST.get('pass')

        user=UserModel.objects.filter(email=e,password=p)
        if(user.count()>0):
            for user in user:
                req.session['email']=user.email
                req.session['id']=user.id
                req.session['name']=user.name
                return redirect('qna:read')
        else:
            return HttpResponse("Wrong CRedentials")

    else:
        return render(req,'login.html')

def logout(req):
    req.session.flush()
    return redirect('user:login')        

