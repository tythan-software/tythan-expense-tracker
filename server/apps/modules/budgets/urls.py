from django.urls import path
from modules.budgets import views

urlpatterns = [
    path('budget/', views.get_budget, name='get_budget'),
    path('budget/create/', views.create_budget, name='create_budget'),
    path('budget/update/<int:pk>/', views.update_budget, name='update_budget'),
    path('budget/delete/<int:pk>/', views.delete_budget, name='delete_budget'),
]
