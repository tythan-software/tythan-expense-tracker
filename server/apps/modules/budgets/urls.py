from django.urls import path
from apps.modules.budgets import views

URL_BASIC = "budgets"

urlpatterns = [
    path(f'{URL_BASIC}', views.get_budget),
    path(f'{URL_BASIC}', views.create_budget),
    path(f'{URL_BASIC}/<int:pk>/', views.update_budget),
    path(f'{URL_BASIC}/<int:pk>/', views.delete_budget),
]
