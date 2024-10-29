
from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
    path('registro/', views.registro_view, name="registro_view"),
    path('login/', views.login_view, name="login_view"),
]