
from django.urls import path,include
from users.views import signup
urlpatterns = [
    path('',signup)
]