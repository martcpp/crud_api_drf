from django.db import models

# Create your models here.

class company (models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.name

class advocate (models.Model):
    company = models.ForeignKey(company, null = True, blank = True, on_delete = models.SET_NULL)
    
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.username