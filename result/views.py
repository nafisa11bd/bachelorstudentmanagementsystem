from django.shortcuts import render,redirect
from result.models import CSE3101
from result.models import CSE3101
from result.form import formcse_3101


def classtest(request):
    return render(request,'result/classtest.html')

def cse3101(request):
    if request.method=="POST":
       form=formcse_3101(request.POST or None)
       if form.is_valid():
           form.save()
       return redirect(cse3101)

    else:
        cse_3101=CSE3101.objects.all
        return render(request,'result/cse3101.html',{'cse_3101':cse_3101})

def deletecse3101(request,cse3101_roll):
    t_delete=CSE3101.objects.get(pk=cse3101_roll)
    t_delete.delete()
    return redirect(cse3101)

def editcse3101(request,cse3101_roll):
    if request.method =="POST":
        cse3101obj = CSE3101.objects.get(pk=cse3101_roll)
        form = formcse_3101(request.POST or None,instance=cse3101obj)
        if form.is_valid():
            form.save()
        return redirect(cse3101)
    else:
        cse3101obj = CSE3101.objects.get(pk=cse3101_roll)
        return render(request, 'edit.html', {'cse3101obj': cse3101obj})



