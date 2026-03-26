from django.db import models

# Create your models here.
class reginfo(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)  

    def __str__(self):
        return self.name