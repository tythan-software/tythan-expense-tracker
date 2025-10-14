from django.urls import path

from modules.users import views

urlpatterns = [
    path("auth/login/", views.login_view, name="login"),
    path("auth/logout/", views.logout_view, name="logout"),
    path("user/", views.register_view, name="register"),
]
