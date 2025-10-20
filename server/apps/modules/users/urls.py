from django.urls import path

from apps.modules.users import views

URL_BASIC = "users"

urlpatterns = [
    path(f"{URL_BASIC}", views.create_view),
    path(f"{URL_BASIC}/<str:username>/", views.delete_user)
]
