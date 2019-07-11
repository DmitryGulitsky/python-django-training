from django.db import models


class AuthorsModel(models.Model):
    class Meta:
        verbose_name = 'AuthorsModel'
        verbose_name_plural = 'AuthorsModels'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
