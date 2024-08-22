from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    register = models.CharField(max_length=30, unique=True)
    birth_date = models.DateField()
    classroom = models.CharField(max_length=20)
    phone = models.PositiveIntegerField(unique=True, blank=True)

    def _str_(self) -> str:
        return f"{self.register} - {self.name}" 
    
