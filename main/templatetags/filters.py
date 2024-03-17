from django import template

register = template.Library()


@register.filter()
def split(s: str):
    return s[:100]
