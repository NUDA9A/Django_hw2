from django import template

register = template.Library()


@register.filter()
def split(s: str):
    return s[:100]


@register.filter()
def my_media(data: str):
    if data:
        return f'/media/{data}'
    return '#'
