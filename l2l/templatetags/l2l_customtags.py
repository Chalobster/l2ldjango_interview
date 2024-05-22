from django import template

register = template.Library()

@register.filter
def l2l_dt(date_to_convert):
    result = ""
    if date_to_convert is not None:
        if type(date_to_convert) is str:
            #"%Y-%m-%dT%H:%M:%S"
            result = date_to_convert
        else:
            #"%Y-%m-%d %H:%M:%S"
            result = date_to_convert.strftime("%Y-%m-%d %H:%M:%S")

    return result