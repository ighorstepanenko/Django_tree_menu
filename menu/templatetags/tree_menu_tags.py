from django import template

from menu.models import MenuItem
from menu.utils import build_menu_tree, get_menu_item_ancestors

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, selected_menu_title):
    menu_items = MenuItem.objects.filter(menu_title__title=selected_menu_title).select_related('parent')
    current_path = context['request'].path_info

    active_item = None
    for item in menu_items:
        if f'/{item.url}/' == current_path:
            active_item = item
            break

    if active_item is not None:
        ancestors = get_menu_item_ancestors(active_item)
        menu_tree = build_menu_tree(menu_items, ancestors)
    else:
        menu_tree = build_menu_tree(menu_items, menu_items)
    return {'menu_title': selected_menu_title, 'menu_tree': menu_tree, 'current_path': current_path}
