"""
URL configuration for finarden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views
from django.views.generic import RedirectView

urlpatterns = [
    path("",RedirectView.as_view(url="/home",permanent=False)),
    path("inicio",RedirectView.as_view(url="/home",permanent=False),name="inicio"),
    path('home', admin.site.urls,name='home'),
    path('usuarios',include('users.urls')),
    path('expends',include('expends.urls')),
    path('converter', views.converter, name='converter')
]
