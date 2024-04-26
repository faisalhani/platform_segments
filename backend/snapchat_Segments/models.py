from django.db import models

# Create your models here.

class CustomerList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    # Add more fields as needed

    def __str__(self):
        return self.name