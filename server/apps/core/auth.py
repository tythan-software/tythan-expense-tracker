"""
Django auth URLs
"""

# Django imports
from django.urls import path

# Local imports
from apps.modules.users import views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
]