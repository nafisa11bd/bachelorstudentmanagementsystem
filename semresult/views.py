from django.shortcuts import render

def frontpage(request):
    return render(request,'semresult/frontpage.html')

def upload(request):
    return render(request,'semresult/upload.html')
