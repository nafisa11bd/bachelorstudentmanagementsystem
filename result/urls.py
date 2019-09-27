from django.urls import path,include
from . import views


urlpatterns = [
    path('classtest',views.classtest,name='classtest'),
    path('cse3101',views.cse3101,name='cse3101'),
]
