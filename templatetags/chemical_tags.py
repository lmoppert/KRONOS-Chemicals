from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.filter
def show_signal(value):
    """Show the word representation of a signal"""
    if value == 'w' or value == u'w':
        s = u'<span class="label label-warning">%s</span>' % _("Warning")
    elif value == 'd' or value == u'd':
        s = u'<span class="label label-danger">%s</span>' % _("Danger")
    else:
        s = u'<span class="label label-default">%s</span>' % _("No Signal")
    return mark_safe(s)


@register.inclusion_tag('chemicals/letter_filter.html')
def letter_filter(letter):
    return {'letter': letter}


@register.inclusion_tag('chemicals/department_filter.html')
def department_filter(plants, target_name):
    return {'plants': plants, 'target_name': target_name}
# coding: utf-8
