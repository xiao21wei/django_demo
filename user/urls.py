from django.urls import path

from .views import *

urlpatterns = [
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("logout", logout, name="logout"),
    path("get_user", get_user, name="get_user"),
    path("update", update, name="update"),
]

