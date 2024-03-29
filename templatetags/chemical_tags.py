# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from collections import OrderedDict
from chemicals.models.periphery import Stock

register = template.Library()


@register.filter
def sort_list(value):
    """Return the given list sorted"""
    if isinstance(value, dict):
        new_dict = OrderedDict()
        key_list = value.keys()
        key_list.sort()
        for key in key_list:
            new_dict[key] = value[key]
        return new_dict
    elif isinstance(value, list):
        new_list = list(value)
        new_list.sort()
        return new_list
    else:
        return value
sort_list.is_safe = True


@register.filter
def show_unit(value):
    """Show the word representation of a unit"""
    if value in Stock.UNITS:
        return Stock.UNITS[value]
    else:
        return ''


@register.filter
def show_signal(value):
    """Show the word representation of a signal"""
    template = u'<span class="label label-{}">{}</span>'
    if value == 'w' or value == u'w':
        html = format_html(template, "warning", _("Warning"))
    elif value == 'd' or value == u'd':
        html = format_html(template, "danger", _("Danger"))
    elif value == 'n' or value == u'n':
        html = format_html(template, "default", _("No Signal"))
    else:
        html = mark_safe('')
    return html


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


@register.inclusion_tag('chemicals/location_filter.html', takes_context=True)
def location_filter(context):
    return {'locations': context["locations"], }


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
