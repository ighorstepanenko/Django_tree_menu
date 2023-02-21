from django import template
from django.http import request
from django.urls import resolve
from ..models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True, name=menu_name).select_related('parent')
    current_url = resolve(request.path_info).url_name

    def draw_menu_items(menu_items, level=0):
        output = ''
        for item in menu_items:
            is_active = False
            sub_menu_items = MenuItem.objects.filter(parent=item)
            if current_url == item.url:
                is_active = True

            output += f'<li class="{"active" if is_active else ""}">' \
                      f'<a href="{item.url}">{item.name}</a>'
            if sub_menu_items:
                output += '<ul>'
                if is_active or level < 2:
                    output += draw_menu_items(sub_menu_items, level=level+1)
                output += '</ul>'
            output += '</li>'
        return output

    return draw_menu_items(menu_items)
