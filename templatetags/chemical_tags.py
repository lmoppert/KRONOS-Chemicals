# -*- coding: utf-8 -*-
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


@register.inclusion_tag('chemicals/letter_filter.html', takes_context=True)
def letter_filter(context, letter):
    params = ""
    for k, v in context["request"].GET.items():
        if not k == "lid":
            params += "&{}={}".format(k, v)
    return {'letter': letter, 'params': params}


@register.inclusion_tag('chemicals/department_filter.html')
def department_filter(plants, target_name):
    return {'plants': plants, 'target_name': target_name}


@register.inclusion_tag('chemicals/max_items.html', takes_context=True)
def max_items(context):
    choices = [10, 25, 100, 200, 500]
    get_params = context["request"].GET
    params = ""
    for k, v in get_params.items():
        if not k == "per_page":
            params += "&{}={}".format(k, v)
    if 'per_page' in get_params:
        per_page = get_params["per_page"]
    else:
        per_page = '25'
    return {
        'per_page': per_page,
        'params': params,
        'choices': choices,
    }
