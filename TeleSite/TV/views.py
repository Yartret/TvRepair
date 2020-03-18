from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def index(request):
    return render(request, 'extendBase/front_page.html')


def send_email(request):
    subject = 'Новая заявка!'
    message = 'Имя: ' + request.POST.get('name_field') + '\n' + 'Телефон\Email: ' + request.POST.get(
        'name_field2') + '\n' + 'Cообщение: ' + request.POST.get('name_field3')
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['RemontTValya@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'extendBase/mail.html')
