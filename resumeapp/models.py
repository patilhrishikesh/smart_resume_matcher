from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name