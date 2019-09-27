from django.urls import path,include
from . import views



urlpatterns = [
    path('signup', views.signup, name ='signup'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    path('student',views.student,name='student'),
    path('teacher', views.teacher,name='teacher'),
    path('courseadvisor',views.courseadvisor,name='courseadvisor'),

]