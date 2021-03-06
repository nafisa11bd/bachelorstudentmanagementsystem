from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('CSE',views.CSE,name='CSE'),
    path('frst_y_cse', views.frst_y_cse, name='frst_y_cse'),
    path('scnd_y_cse', views.scnd_y_cse, name='scnd_y_cse'),
    path('thrd_y_cse', views.thrd_y_cse, name='thrd_y_cse'),
    path('frth_y_cse', views.frth_y_cse, name='frth_y_cse'),
    path('frstycseA', views.frstycseA, name='frstycseA'),
    path('frstycseB', views.frstycseB, name='frstycseB'),
    path('frstycseC', views.frstycseC, name='frstycseC'),
    path('scndcseA', views.scndcseA, name='scndcseA'),
    path('scndcseB', views.scndcseB, name='scndcseB'),
    path('thrdcseA', views.thrdcseA, name='thrdcseA'),
    path('thrdcseB', views.thrdcseB, name='thrdcseB'),
    path('frthcseA', views.frthcseA, name='frthcseA'),
    path('frthcseB', views.frthcseB, name='frthcseB'),
    path('CSE1101', views.CSE1101, name='CSE1101'),
    path('CSE1101s', views.CSE1101s, name='CSE1101s'),
    path('delete/<cse1101_roll>', views.deletecse1101, name='deletecse1101'),
    path('edit/<int:cse1101_roll>', views.editcse1101, name='editcse1101'),
]