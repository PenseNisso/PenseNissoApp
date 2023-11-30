from django import template

register = template.Library()


@register.filter(is_safe=True)
def url_fix(value):
    return value.replace(
        "<a ", "<a class='underline text-blue-500 visited:text-purple-600'"
    )
