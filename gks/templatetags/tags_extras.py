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
    color_rgb = [(120, 0, 0), (0, 120, 0), (0, 0, 120), (225, 225, 0), (225, 0, 225), (225, 120, 120)]
    return color_rgb[num-1]


@register.filter(name='legend_x')
def legend_x(k):
    return 50 + 100 * k


@register.filter(name='legend_text')
def legend_x(k):
    return 100 + 100 * k


