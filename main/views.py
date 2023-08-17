from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . models import Project, Blog, Course
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def homepage(request):
    project = Project.objects.all()
    blog = Blog.objects.all()
    course = Course.objects.all()
    context = {
        'projects': project,
        'blogs' : blog,
        'courses' :course
    }
    return render(request, 'main/home.html', context=context )


def send_mail(request):
    if request.method == 'POST':

        last_name = request.POST.get('lastname', "")
        first_name = request.POST.get('firstname', "")
        email = request.POST.get('mail', "")
        message = request.POST.get('message',"")
        context = { 'emil':email, 'first_name':first_name,'last_name':last_name, 'message': message}
        
        send_mail(
            'From online Portfolio', # title
            message, # message
            settings.EMAIL_HOST_USER, # from who email
            ['thmotuk@gmail.com'], # to who email 
            fail_silently=True
        )
        return redirect('homepage')
    
    else:
        return render(request, 'main/home.html', {})