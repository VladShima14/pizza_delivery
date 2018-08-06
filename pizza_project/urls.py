"""pizza_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from pizza_app_auth import urls as pizza_auth_urls
from pizza_app import urls as pizza_urls
from pizza_app.views import index
from rest_api_app import urls as rest_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^auth/', include(pizza_auth_urls, namespace='auth_app')),
    url(r'^pizza/', include(pizza_urls, namespace='pizza')),
    url(r'^$', index, name='index'),
    url(r'^api/v1/', include(rest_urls, namespace="rest_api")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
