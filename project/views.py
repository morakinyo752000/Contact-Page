from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from email.mime import multipart, text
from email.utils import formataddr
from django.conf import settings
import smtplib, ssl

# Create your views here.


def index(request):
    if not request.method == 'POST':
        return render(request, 'index.html', {})
    name = request.POST['name']
    reciever = request.POST['email']
    sender = settings.EMAIL_HOST_USER
    email_subject = request.POST['subject']
    message_in = request.POST['message']
    complete_message = f'Hi There{name}! \n ,  Thank You for contacting us. This is your message: \n \n {message_in}'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        message = multipart.MIMEMultipart()
        message.attach(text.MIMEText(complete_message, 'plain'))
        message["To"] = reciever
        from_email = sender
        message['Subject'] = email_subject
        message['From'] = formataddr(('localhost.com', from_email))
        server.sendmail(
            from_email,
            reciever,
            message.as_string())

    return redirect('/')


