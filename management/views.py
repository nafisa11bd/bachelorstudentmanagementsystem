from django.shortcuts import render, redirect
from .models import Courseregister
from .models import Courseregister2

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
def home(request):
    return render(request,'management/home.html')




def routines(request):
    return render(request,'routines.html')


def courseregister(request):
    if request.method == 'POST':
        if request.POST['fname'] and request.POST['lname'] and request.POST['roll'] and request.POST['dept'] and request.POST['roll'] and request.POST['regno'] and request.POST['year'] and request.POST['sem'] and request.POST['cno1'] and request.POST['coname1'] and request.POST['cno2'] and request.POST['coname2'] and request.POST['cno3'] and request.POST['coname3']:
            
            try:
                user = Courseregister.objects.get(roll=request.POST['roll'])
                return render(request, 'management/registerform.html',{'error':'This student has already been existed!'})
            except Courseregister.DoesNotExist:              
                obj = Courseregister()

                obj.fname = request.POST['fname']
                obj.lname = request.POST['lname']
                obj.dept = request.POST['dept']
                obj.email = request.POST['email']
                
                obj.roll = request.POST['roll']
                obj.regno = request.POST['regno']
                obj.pec = request.POST['pec']
                
                if int(request.POST['year']) > 0 and int(request.POST['year']) <= 4:
                    obj.year = request.POST['year']
                else:
                    return render(request, 'management/registerform.html', {'error':'Year must be between 1 and 4'})
                if int(request.POST['sem']) > 0 and int(request.POST['sem']) <= 2: 
                    obj.semester = request.POST['sem']
                else:
                    return render(request, 'management/registerform.html', {'error':'Semester must be between 1 and 2'})

                
                obj.cno1 = request.POST['cno1']
                obj.cname1 = request.POST['coname1']
                obj.cno2 = request.POST['cno2']
                obj.cname2 = request.POST['coname2']
                obj.cno3 = request.POST['cno3']
                obj.cname3 = request.POST['coname3']
                obj.cno4 = request.POST['cno4']
                obj.cname4 = request.POST['coname4']
                obj.cno5 = request.POST['cno5']
                obj.cname5 = request.POST['coname5']

                obj.save()
                
                messages.success(request, 'Your submission for course-registration is completed!')
                return redirect('home')
                def email(request):
                    subject = 'Confirmation for course-registration'
                    message = ' You are accepted for the cources. Welcome to the world of knowledge. '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [obj.email,settings.EMAIL_HOST_USER]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('home')

        else:

            return render (request,'management/registerform.html',{'error':'All Field must be filled up'})
        
            #return redirect('home')
    else:
        return render(request, 'management/registerform.html')


def courseregister2(request):
    if request.method == 'POST':
        if request.POST['fname'] and request.POST['lname'] and request.POST['roll'] and request.POST['dept'] and request.POST['roll'] and request.POST['regno'] and request.POST['year'] and request.POST['sem'] and request.POST['cno1'] and request.POST['coname1'] and request.POST['cno2'] and request.POST['coname2'] and request.POST['cno3'] and request.POST['coname3']:
            
            try:
                user = Courseregister2.objects.get(roll=request.POST['roll'])
                return render(request, 'management/registerform.html',{'error':'This student has already been existed!'})
            except Courseregister2.DoesNotExist:              
                obj = Courseregister2()
                obj.fname = request.POST['fname']
                obj.lname = request.POST['lname']
                obj.dept = request.POST['dept']
                obj.roll = request.POST['roll']
                obj.regno = request.POST['regno']
                obj.pec = request.POST['pec']
                
                if int(request.POST['year']) > 0 and int(request.POST['year']) <= 4:
                    obj.year = request.POST['year']
                else:
                    return render(request, 'management/registerform.html', {'error':'Year must be between 1 and 4'})
                if int(request.POST['sem']) > 0 and int(request.POST['sem']) <= 2: 
                    obj.semester = request.POST['sem']
                else:
                    return render(request, 'management/registerform.html', {'error':'Semester must be between 1 and 2'})

                obj.cno1 = request.POST['cno1']
                obj.cname1 = request.POST['coname1']
                obj.cno2 = request.POST['cno2']
                obj.cname2 = request.POST['coname2']
                obj.cno3 = request.POST['cno3']
                obj.cname3 = request.POST['coname3']
                obj.cno4 = request.POST['cno4']
                obj.cname4 = request.POST['coname4']
                obj.cno5 = request.POST['cno5']
                obj.cname5 = request.POST['coname5']

                obj.save()
                
                messages.success(request, 'Your course registration is completed!')
                return redirect('home')
        else:

            return render (request,'management/registerform.html',{'error':'All Field must be filled up'})
        
            #return redirect('home')
    else:
        return render(request, 'management/registerform.html')

def reghome(request):
    return render(request,'management/reghome.html')