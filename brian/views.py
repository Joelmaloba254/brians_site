from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

def home(request):
    return render(request, 'brian/home.html')

def about(request):
    return render(request, 'brian/about.html')

def services(request):
    return render(request, 'brian/services.html')

def testimonials(request):
    return render(request, 'brian/testimonials.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Here you can add the logic to send an email or save the message to the database
        send_mail(
            f"Message from {name}: {subject}",
            message,
            email,
            ['brian@example.com'],  # This should be Brian's email
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return HttpResponseRedirect(reverse('contact'))

    return render(request, 'brian/contact.html')
