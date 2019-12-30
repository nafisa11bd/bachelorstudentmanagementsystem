from django.shortcuts import render,redirect
from attendance.models import days
from attendance.form import formdays

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

def CSE1101(request):
    if request.method=="POST":
       form=formdays(request.POST or None)
       if form.is_valid():
           form.save()
       return redirect(CSE1101)

    else:
        p=days.objects.all
        return render(request,'attendance/CSE1101.html',{'d':p})
        
def CSE1101s(request):
    if request.method=="POST":
       form=formdays(request.POST or None)
       if form.is_valid():
           form.save()
       return redirect(CSE1101s)

    else:
        p=days.objects.all
        return render(request,'attendance/CSE1101s.html',{'d':p})

def deletecse1101(request,cse1101_roll):
    t_delete=days.objects.get(pk=cse1101_roll)
    t_delete.delete()
    return redirect(CSE1101)

def editcse1101(request,cse1101_roll):
    if request.method =="POST":
        cse1101obj = days.objects.get(pk=cse1101_roll)
        form = formdays(request.POST or None,instance=cse1101obj)
        if form.is_valid():
            form.save()
        return redirect(CSE1101)
    else:
        cse1101obj = days.objects.get(pk=cse1101_roll)
        return render(request, 'edit.html', {'cse1101obj': cse1101obj})