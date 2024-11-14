from django.db import models

# Create your models here.

class Registrant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interest = models.CharField(max_length=50, choices=[
        ('software-development', 'Software Development'),
        ('cybersecurity', 'Cybersecurity'),
        ('data-science', 'Data Science'),
        ('ai', 'Artificial Intelligence'),
    ])
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
