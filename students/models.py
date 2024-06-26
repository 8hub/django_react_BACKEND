from django.db import models

class Student(models.Model):
    name = models.CharField("Name",max_length=100)
    email = models.EmailField()
    document = models.CharField("Document", max_length=100)
    phone = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration date", auto_now_add=True)

    def __str__(self):
        return self.name