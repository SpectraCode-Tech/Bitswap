from django.contrib import admin
from .models import FAQ, ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter =('name', 'email', 'created_at')
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'is_active', 'created_at')
    search_fields = ('question', 'answer', 'is_active')
    list_filter =('question', 'answer', 'created_at')

