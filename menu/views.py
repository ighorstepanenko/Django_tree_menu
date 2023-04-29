from django.views.generic import ListView

from menu.models import MenuItem


class MenuView(ListView):
    model = MenuItem
    template_name = 'menu/example.html'


class MenuItemView(ListView):
    model = MenuItem
    template_name = 'menu/example.html'
