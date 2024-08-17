from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request, 'base/index.html') 

def products(request):
    return render(request, 'base/products.html')
def about(request):
    return render(request, 'base/ourstory.html')

def services(request): 
    return render(request, 'base/services.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                f"Contact Form Submission from {name}",
                message,
                email,  # From email
                ['kimutaicosmas547@gmail.com'],  # To email
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'base/contact.html', {'form': form})

# def contact(request):
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subject = 'Email To Amazon Filters '
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email, ]
#         send_mail(subject,message,email_from, recipient_list)
    
#     return render(request, 'base/contact.html')