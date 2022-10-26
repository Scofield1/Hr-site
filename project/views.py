import os
from email import message
from re import template
from .models import *

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def opportunities(request):
    return render(request, 'main/oportunities.html')


def email_frontend(request):
    if request.method == 'POST':
        if Registered_mail.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'We already have your resume in our database')
            return redirect('opportunities')
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            file = request.FILES['file']
            template = loader.get_template('resume_form.txt')

            save_mail = Registered_mail(email=email)
            save_mail.save()

            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'message': messages,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                'Frontend - Candidate', message,
                'Frontend Opportunity',
                [os.getenv('EMAIL_HOST_USER')]
            )
            email.content_subtype = 'html'
            email.attach(file.name, file.read(),file.content_type)
            email.send()
            messages.success(request, 'Frontend resume succefully!')
            return redirect('/')
def email_backend(request):
    if request.method == 'POST':
        if Registered_mail.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'We already have your resume in our database')
            return redirect('opportunities')
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            file = request.FILES['file']
            template = loader.get_template('resume_form.txt')

            save_mail = Registered_mail(email=email)
            save_mail.save()

            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'message': messages,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                'Backend - Candidate', message,
                'Backend Opportunity',
                [os.getenv('EMAIL_HOST_USER')]
            )
            email.content_subtype = 'html'
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'Backend resume succefully!')
            return redirect('/')


def email_fullstack(request):
    if request.method == 'POST':
        if Registered_mail.objects.filter(email=request.POST['email']).exists():
            messages.error(request, 'We already have your resume in our database')
            return redirect('opportunities')
        else:
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            experience = request.POST.get('experience')
            file = request.FILES['file']
            template = loader.get_template('resume_form.txt')

            save_mail = Registered_mail(email=email)
            save_mail.save()

            context = {
                'name': name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address,
                'experience': experience,
                'message': messages,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                'Fullstack - Candidate', message,
                'Fullstack Opportunity',
                [os.getenv('EMAIL_HOST_USER')]
            )
            email.content_subtype = 'html'
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, 'Fullstack resume succefully!')
            return redirect('/')
