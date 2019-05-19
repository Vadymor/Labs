from django import template
import random

register = template.Library()


@register.filter(name='position')
def position(pos):
    return 45 + 40 * pos


@register.filter(name='y_pos')
def y_pos(pos):
    return 140 + 40 * pos


@register.filter(name='x_pos')
def x_pos(pos):
    return 50 + 40 * pos[0]


@register.filter(name='length')
def length(pos):
    return 40 * (pos[1] - pos[0])


@register.filter(name='color')
def color(num):
    color = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
    return color
