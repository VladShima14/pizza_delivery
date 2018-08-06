from pizza_app_auth.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "favourite_pizza",
        )
