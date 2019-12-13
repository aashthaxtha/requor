

from django.urls import path
from .views import loginauth,logout

app_name='user'

urlpatterns = [
      path('login/',loginauth,name='login'),
      path('logout/',logout,name='logout')
 ]
