from django.urls import path
from .views import home, register_user, logout_user

urlpatterns = [
    path("", home, name="home"),
        path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
]
