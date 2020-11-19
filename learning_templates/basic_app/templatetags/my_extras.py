from django import template

register = template.Library()

def cut_template_filter(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cut_filter', cut_template_filter)