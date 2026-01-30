from django import template

register = template.Library()


@register.filter(name='length_is')
def length_is(value, arg):
    """Forward-ported from the older implementation of length_is that was replaced by `length`"""
    try:
        return len(value) == int(arg)
    except (ValueError, TypeError):
        return ""
