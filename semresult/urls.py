from django.urls import path,include
from . import views

urlpatterns = [
    path('frontpage',views.frontpage,name='frontpage'),
    path('upload',views.upload,name='upload'),
    path('<int:result_id>',views.details,name='details')

]