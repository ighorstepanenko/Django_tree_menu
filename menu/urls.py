from django.urls import path

from menu.views import MenuView, MenuItemView

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('<str:url>/', MenuItemView.as_view(), name='menu_item'),
    ]