from django.contrib import admin

from .models import Menu, MenuItem


class MenuInstanceInline(admin.TabularInline):
    model = MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_items')
    list_filter = ('title',)
    inlines = [MenuInstanceInline]


class MenuItemInstanceInline(admin.TabularInline):
    model = MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('item',)}
    list_display = ['menu_title', 'item', 'order', 'url', 'parent']
    list_editable = ['item', 'order', 'url', 'parent']
    inlines = [MenuItemInstanceInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
