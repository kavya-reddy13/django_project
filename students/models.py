


from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    address=models.TextField()
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name