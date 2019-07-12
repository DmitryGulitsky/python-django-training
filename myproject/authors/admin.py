from django.contrib import admin

from .models import AuthorsModel

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', )


admin.site.register(AuthorsModel, AuthorAdmin)
