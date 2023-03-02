from django import template

from menu_app.models import Menu

register = template.Library()


@register.inclusion_tag("inc/draw_menu.html")
def draw_menu(menu_name):
    menu = Menu.objects.get(name=menu_name)
    parents = get_parents(menu)
    menu_items = menu.menu_set.all()
    return {
        "menu_items": menu_items,
        "parents": parents,
    }


def get_parents(menu):
    parents = [
        menu,
    ]
    while menu.parent:
        parents = [menu.parent] + parents
        menu = menu.parent
    return parents
