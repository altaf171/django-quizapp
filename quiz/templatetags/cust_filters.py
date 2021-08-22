from django import template
from django.utils import safestring
register = template.Library()

@register.filter(name='aclasses')
def add_classes(value,class_names):

    print(type(value), end='\n\n\n')

    css_classes = value.field.widget.attrs.get('class','')
    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []

    class_names_list = class_names.split(' ')
    for class_name in class_names_list:
        if class_name not in css_classes:
            css_classes.append(class_name)
    
    return value.as_widget(attrs={'class': ' '.join(css_classes)})

@register.filter(is_safe=True)
def addplaceholder(value,placeholder_text):

    print(type(value), end='\n\n\n')

    # get_palcehollder_text = value.strip()

    # get_palcehollder_text = get_palcehollder_text.field.widget.attrs.get('palceholder','')
    # if get_palcehollder_text:
    #     return
    return value.as_widget(attrs={'placeholder':placeholder_text})