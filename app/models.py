from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField()

    duration = models.CharField(max_length=50)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name