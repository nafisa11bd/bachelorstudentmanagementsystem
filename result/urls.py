from django.urls import path,include
from . import views


urlpatterns = [
    path('classtest',views.classtest,name='classtest'),
    path('cse3101',views.cse3101,name='cse3101'),
    path('cse3101s',views.cse3101s,name='cse3101s'),
    path('delete/<cse3101_roll>', views.deletecse3101, name='deletecse3101'),
    path('edit/<int:cse3101_roll>', views.editcse3101, name='editcse3101'),

]
