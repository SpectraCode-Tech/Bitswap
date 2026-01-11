from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

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