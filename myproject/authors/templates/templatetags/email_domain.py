from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# filter only string type values
@stringfilter
@register.filter(name='domain')
def cut_email_domain(value):
    if '@' in value:
        return '(email not stated)'
    return value.partition('@')[2]
