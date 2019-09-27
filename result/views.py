from django.shortcuts import render


def classtest(request):
    return render(request,'result/classtest.html')

def cse3101(request):
    return render(request,'result/cse3101.html')
