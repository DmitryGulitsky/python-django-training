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


class StudentInfo(models.Model):

    class Meta:
        verbose_name = "StudentInfo"
        verbose_name_plural = "StudentInfos"

    pass_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info'
    )

    def __str__(self):
        return f'{self.pass_id}'

#


class Publisher(models.Model):

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=250)
    # body = models.TextField()
    pub_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.title} on {self.pub_date}'
