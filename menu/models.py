from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название меню')

    def display_items(self):
        """Creates a string for the MenuItems. This is required to display items in Admin."""
        return ', '.join([suitable.item for suitable in MenuItem.objects.filter(menu_title=self)])

    display_items.short_description = 'Пункты данного меню'

    class Meta:
        verbose_name = 'Название меню'
        verbose_name_plural = 'Меню'
        ordering = ['title']

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu_title = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', verbose_name='Меню')
    item = models.CharField(max_length=255, verbose_name='Название пункта меню')
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name='Надпункт меню')
    order = models.PositiveIntegerField(default=0, verbose_name='Уровень вложенности')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['menu_title', 'order']

    def __str__(self):
        return self.item


