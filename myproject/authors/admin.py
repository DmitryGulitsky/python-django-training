from django.contrib import admin

from .models import AuthorsModel


@admin.register(AuthorsModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'email_domain', 'abc')

    empty_value_display = '(email not stated)'

    def abc(self, object):
        return

    def email_domain(self, obj):
        if obj.email is not None:
            return obj.email.partition('@')[2]

    email_domain.empty_value_display = '[email not stated]'

#admin.site.register(AuthorsModel, AuthorAdmin)
