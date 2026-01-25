from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import FAQ

# Create your views here.
def home(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'index.html', {'faqs' : faqs})

def about(request):
    return render(request, 'about.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            send_mail(
                subject=f"New Contact Message: {contact.subject}",
                message=f"""
                Name: {contact.name}
                Email: {contact.email}
                Message: 
                {contact.message}
                """,
                
                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def faq(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'faq.html', {'faqs': faqs})

def feature(request):
    return render(request, 'feature.html')

def roadmap(request):
    return render(request, 'roadmap.html')

def service(request):
    return render(request, 'service.html')

def token(request):
    return render(request, 'token.html')

def notFound(request):
    return render(request, '404.html')