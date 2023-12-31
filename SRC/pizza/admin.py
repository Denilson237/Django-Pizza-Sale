from django.contrib import admin
from pizza.models import menu
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ('nom',)
admin.site.register(menu, PizzaAdmin)