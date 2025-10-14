from django.urls import include, path

app_name = "apps.core"

urlpatterns = [
    path('api/', include('modules.users.urls'), name='users'),
    path('api/', include('modules.budgets.urls'), name='budgets'),
    path('api/', include('modules.expenses.urls'), name='expenses'),
]