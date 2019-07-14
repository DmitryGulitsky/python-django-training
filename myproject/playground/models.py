from django.db import models


class StudentInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pass_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
