from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.courseregister, name='courseregister'),

    

    path('register2/', views.courseregister2, name='courseregister2'),
    path('reghome/', views.reghome, name='reghome'),


]


