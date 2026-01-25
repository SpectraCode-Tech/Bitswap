from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField()
    subject = models.CharField(max_length = 200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=225)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.question
