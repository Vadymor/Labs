from django import template

register = template.Library()


@register.filter(name='position')
def position(pos):
    return 45 + 40 * pos
