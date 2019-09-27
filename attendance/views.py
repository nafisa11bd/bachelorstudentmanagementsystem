from django.shortcuts import render

def index(request):
    return render(request,'attendance/index.html')

def CSE(request):
    return render(request,'attendance/CSE.html')

def frst_y_cse(request):
    return render(request,'attendance/frst_y_cse.html')

def scnd_y_cse(request):
    return render(request,'attendance/scnd_y_cse.html')

def thrd_y_cse(request):
    return render(request,'attendance/thrd_y_cse.html')

def frth_y_cse(request):
    return render(request,'attendance/frth_y_cse.html')

def frstycseA(request):
    return render(request,'attendance/frstycseA.html')

def frstycseB(request):
    return render(request,'attendance/frstycseB.html')

def frstycseC(request):
    return render(request,'attendance/frstycseC.html')

def scndcseA(request):
    return render(request,'attendance/scndcseA.html')

def scndcseB(request):
    return render(request,'attendance/scndcseB.html')

def thrdcseA(request):
    return render(request,'attendance/thrdcseA.html')

def thrdcseB(request):
    return render(request,'attendance/thrdcseB.html')

def frthcseA(request):
    return render(request,'attendance/frthcseA.html')

def frthcseB(request):
    return render(request,'attendance/frthcseB.html')



