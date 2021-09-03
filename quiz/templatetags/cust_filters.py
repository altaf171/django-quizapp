
from django import template
from django.utils import safestring
register = template.Library()



'''
getting individual element of dict in template

'''

@register.filter
def dictitem(d, key):
    # print('key:',key, type(key))
    # key_str = str(key)
    # print('keystr:',key_str, type(key_str))
    
    try:
       item= d[key]
    except(KeyError):
        item = ' '
    # print(item)
    return item
