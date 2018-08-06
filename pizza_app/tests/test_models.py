from django.test import TestCase
from pizza_app.models import PizzaSize, PizzaIngredient, Address


class TestPizzaSize(TestCase):
    def test_pizza_size_create(self):
        pizza_size = PizzaSize.objects.create(
            size=PizzaSize.SMALL[0]
        )
        assert pizza_size.pk is not None


class TestPizzaIngredient(TestCase):
    @classmethod
    def setUp(cls):
        cls.address = Address.objects.create(
            full='Ukraine, Dnipro'
        )

    def test_create_pizza_ingredient(self):
        ingredient = PizzaIngredient.objects.create(name='test')
        assert ingredient.pk is not None

    def test_get_pizza_ingredient(self):
        ingredient = PizzaIngredient.objects.get(name='Cheese')
        assert ingredient is not None

