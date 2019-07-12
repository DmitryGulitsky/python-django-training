from django.db import models


class AuthorsModel(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
