
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



'''
not using this anymore because two filters not working together
apparently value.as_widget converts the output into safestring format

'''

# @register.filter(name='aclasses')
# def add_classes(value, class_names):

#     print(type(value), end='\n\n\n')

#     css_classes = value.field.widget.attrs.get('class', '')
#     # check if class is set or empty and split its content to list (or init list)
#     if css_classes:
#         css_classes = css_classes.split(' ')
#     else:
#         css_classes = []

#     class_names_list = class_names.split(' ')
#     for class_name in class_names_list:
#         if class_name not in css_classes:
#             css_classes.append(class_name)

#     return value.as_widget(attrs={'class': ' '.join(css_classes)})


# @register.filter(is_safe=True)
# def addplaceholder(value, placeholder_text):

#     print(type(value), end='\n\n\n')

#     # get_palcehollder_text = value.strip()

#     # get_palcehollder_text = get_palcehollder_text.field.widget.attrs.get('palceholder','')
#     # if get_palcehollder_text:
#     #     return
#     return value.as_widget(attrs={'placeholder': placeholder_text})





# @register.filter
# def member(obj, name):
#     return getattr(obj, name, None)
