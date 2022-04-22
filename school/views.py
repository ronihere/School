from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import details, notice , to_do, all_urls, upcomingevents
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(requests):
    return render(requests,'index.html')
def admin_(requests):
    works=to_do.objects.all()
    return render(requests,'admin_.html',{'works':works})
def delete_todo(request,id):
    a=id
    to_do.objects.filter(id=a).delete()
    return redirect('/contactus')
def course_notice(requests):
    notices = notice.objects.all()
    return render(requests,'notice.html',{'notices':notices})
def faqs(requests):
    return render(requests,'faqs.html')
def faculty(requests):
    return render(requests,'faculty.html')
def form(requests):
    return render(requests,'form.html')
def show(requests):
    name=requests.POST['name']
    gender=requests.POST['gender']
    email= requests.POST['email']
    education=requests.POST['education']
    DOB=requests.POST['dob']
    contact=requests.POST['contact']
    age=requests.POST['age']
    address=requests.POST['address']
    if User.objects.filter(email=email).first():
        messages.error(requests, f"{email}, You are already enrolled ! ")
        return redirect('/')
    else:
        ins= details(name=name,gender=gender,email=email,education=education,contact=contact,age=age,address=address)
        ins.save()
        send_mail("TMS-Kolkata",
                f"Hey {name}! Congratulations.You have successfully submitted your enrollment form .You will listen from us soon. Thank you."
                f'\n Details given by you:\n NAME : {name}\n GENDER: {gender} \n DOB:{DOB}\n EMAIL: {email} \n EDUCATION: {education} \n PHONE: {contact}\n'
                f' AGE: {age}\n ADDRESS: {address}',
                'from0the0headquarter0of@gmail.com',
                [email],
                fail_silently=True)

        messages.info(requests,f"Congratulations {name} !, You have successfully enrolled")
        return redirect('/')
def links(requests):
    all_links=all_urls.objects.all()
    return render(requests,'links.html',{'params':all_links})
def upcoming_events(request):
    events = upcomingevents.objects.all()
    return render(request,'upcomingevents.html',{"events":events})
def covid(request):
    return render(request,'covid_index.html')