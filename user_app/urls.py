

from django.urls import path,include
from .views impor qna_app,user_app

urlpatterns = [
    
    path('qna/',qna_app),
    path('user/',user_app)
]
