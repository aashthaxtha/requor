"""requor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from .views import addques,question,question_detail,update_question,test,delete,QuestionModelCreateView,QuestionModelListView,upvote
# from .views import qna_app,user_app

app_name = 'qna'

urlpatterns = [
    path('addques/',addques,name='addques'),
    path('read/',question,name='read'),
    path('update/<int:id>/',update_question,name='update_question'),
    path('create/',addques,name='addques'),
    path('delete/<int:id>/',delete,name='delete'),
    path('create/',QuestionModelCreateView.as_view()),
    path('list/',QuestionModelListView.as_view()),
    path('upvote/<int:id>/',upvote,name='upvote'),
    # path('addans/<int:id>',addans,name='addans')
    path('detail/<int:id>/',question_detail,name='detail'),
    path('test/<int:id>/',test,name='qna.test')

   

# url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),


    
]
