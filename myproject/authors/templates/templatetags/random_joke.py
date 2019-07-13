from random import choice
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


jokes = [
    'Aliquam architecto ducimus hic illo illum modi necessitatibus praesentium totam ut voluptate.',
    'Beatae cupiditate dolor eius eos harum ipsam nostrum numquam, optio provident tempora.',
    'Adipisci consequuntur dolorum, ducimus earum explicabo incidunt minima quas quo reiciendis reprehenderit.',
]


@register.simple_tag
def joke(index=None):
    if index is None or not isinstance(index, int) or index >= len(jokes):
        a_joke = choice(jokes)
    else:
        a_joke = jokes(index)
    return mark_safe(f'<p>{a_joke}</p>')
