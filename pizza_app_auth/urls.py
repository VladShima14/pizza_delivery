from django.conf.urls import url

from django.contrib.auth.views import login, logout_then_login
from django.views.generic import CreateView

from pizza_app_auth.forms import CustomCreationForm


urlpatterns = [
    url(r'^login/', login, {'template_name': 'auth_app/login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=CustomCreationForm,
        success_url='/',
    ), name='register'),

]
