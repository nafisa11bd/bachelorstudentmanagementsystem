from django.shortcuts import render,redirect,get_object_or_404
from .models import Result

def frontpage(request):
    result=Result.objects
    return render(request,'semresult/frontpage.html',{'result':result})

def upload(request):
    if request.method == 'POST':
        if request.POST['title'] and request.FILES['file']:
            result=Result()
            result.title=request.POST['title']
            result.file=request.FILES['file']
            result.save()
            return redirect('/semresult/'+str(result.id))
        else:
            return render(request, 'semresult/upload.html', {'error': 'All fields are required.'})


    else:
        return render(request,'semresult/upload.html')

def details(request,result_id):
    result=get_object_or_404(Result,pk=result_id)
    return render(request,'semresult/details.html',{'result':result})