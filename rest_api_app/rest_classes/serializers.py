from rest_framework import serializers
from pizza_app_auth.models import CustomUser
from pizza_app.models import PizzaMenuItem, PizzaIngredient


class PizzaMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    # ingredients = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    #  )
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=PizzaIngredient.objects.all())

    class Meta:
        model = PizzaMenuItem
        fields = ('id', 'name', 'ingredients')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id',
                  'username',
                  'email',
                  'our_note',
                  'favourite_pizza',
                  )

    favourite_pizza = serializers.SlugRelatedField(slug_field='name', queryset=PizzaMenuItem.objects.all())

    # def create(self, validated_data):
    #     return album
    #
    # def update(self, instance, validated_data):

