from django import template

register = template.Library()

@register.filter
def key(d, key_name):
    try:
        return d[key_name]
    except KeyError:
        return None
