from datetime import datetime
from django import template

register = template.Library()

@register.filter
def l2l_dt(date_to_convert):
    result = "incorrect data type"
    if date_to_convert is not None:
        if type(date_to_convert) is str:
            #"%Y-%m-%dT%H:%M:%S"
            result = dt = datetime.strptime(date_to_convert, "%Y-%m-%dT%H:%M:%S")
            result = dt.strftime("%Y-%m-%dT%H:%M:%S")
        elif type(date_to_convert) is datetime:
            #"%Y-%m-%d %H:%M:%S"
            result = date_to_convert.strftime("%Y-%m-%d %H:%M:%S")

    return result