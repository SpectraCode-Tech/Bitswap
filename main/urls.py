from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('faq/', views.faq, name = 'faq'),
    path('feature/', views.feature, name = 'feature'),
    path('roadmap/', views.roadmap, name = 'roadmap'),
    path('service/', views.service, name = 'service'),
    path('token/', views.token, name = 'token'),
    path('404/', views.notFound, name = 'notFound'),
]