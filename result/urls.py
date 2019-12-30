from django.urls import path,include
from . import views


urlpatterns = [
    path('classtest',views.classtest,name='classtest'),
    path('cse3101',views.cse3101,name='cse3101'),
    path('cse3101s', views.cse3101s, name='cse3101s'),
    path('delete/<cse3101_roll>', views.deletecse3101, name='deletecse3101'),
    path('edit/<int:cse3101_roll>', views.editcse3101, name='editcse3101'),
    path('cse', views.cse, name='cse'),
    path('firstyearcse', views.firstyearcse, name='firstyearcse'),
    path('secondyearcse', views.secondyearcse, name='secondyearcse'),
    path('thirdyearcse', views.thirdyearcse, name='thirdyearcse'),
    path('fourthyearcse', views.fourthyearcse, name='fourthyearcse'),
    path('thirdyearfirstsemcse', views.thirdyearfirstsemcse, name='thirdyearfirstsemcse'),
    path('cse3103', views.cse3103, name='cse3103'),
    path('delete/<cse3103_roll>', views.deletecse3103, name='deletecse3103'),
    path('edit/<int:cse3103_roll>', views.editcse3103, name='editcse3103'),



]
