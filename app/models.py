from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(unique=True)
    number=models.CharField(max_length=15)
    subject=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name