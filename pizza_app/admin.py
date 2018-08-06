from django.contrib import admin
from .models import Address, PizzaMenuItem, PizzaSize, PizzaIngredient, PizzaOrder
from .forms import PizzaOrderForm
# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full',)


class PizzaSizeModel(admin.ModelAdmin):
    list_display = ('size', )


admin.site.register(PizzaSize, PizzaSizeModel)


class PizzaIngredientModel(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(PizzaIngredient, PizzaIngredientModel)


class PizzaOrderModel(admin.ModelAdmin):
    list_display = ('kind', 'size', 'delivered')
    form = PizzaOrderForm

    def has_add_permission(self, request):
        return False


admin.site.register(PizzaOrder, PizzaSizeModel)
