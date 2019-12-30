from django.shortcuts import render,redirect
from result.models import CSE3101
from result.models import CSE3103
from result.models import CSE3105
from result.models import CSE3107
from result.models import CSE3109

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

def cse3101s(request):
    if request.method=="POST":
       form=formcse_3101(request.POST or None)
       if form.is_valid():
           form.save()
       return redirect(cse3101)

    else:
        cse_3101=CSE3101.objects.all
        return render(request,'result/cse3101s.html',{'cse_3101':cse_3101})

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
            cse3101obj.save()



        return redirect(cse3101)
    else:
        cse3101obj = CSE3101.objects.get(pk=cse3101_roll)
        return render(request, 'edit.html', {'cse3101obj': cse3101obj})

def cse(request):
    return render(request, 'result/cse.html')

def firstyearcse(request):
    return render(request, 'result/firstyearcse.html')

def secondyearcse(request):
    return render(request, 'result/secondyearcse.html')

def thirdyearcse(request):
    return render(request, 'result/thirdyearcse.html')

def fourthyearcse(request):
    return render(request, 'result/fourthyearcse.html')

def thirdyearfirstsemcse(request):
    return render(request,'result/thirdyearfirstsemcse.html')

def cse3103(request):
    if request.method=="POST":
       form=formcse_3101(request.POST or None)
       if form.is_valid():
           form.save()
       return redirect(cse3103)

    else:
        cse_3103=CSE3103.objects.all
        return render(request,'result/cse3103.html',{'cse_3103':cse_3103})

def deletecse3103(request,cse3103_roll):
    t_delete=CSE3103.objects.get(pk=cse3103_roll)
    t_delete.delete()
    return redirect(cse3103)

def editcse3103(request,cse3103_roll):
    if request.method =="POST":
        cse3103obj = CSE3103.objects.get(pk=cse3103_roll)

        form = formcse_3103(request.POST or None,instance=cse3103obj)
        if form.is_valid():
            form.save()

        cse3103obj.save()

        return redirect(cse3103)
    else:
        cse3103obj = CSE3103.objects.get(pk=cse3103_roll)
        return render(request, 'edit.html', {'cse3103obj': cse3103obj})


