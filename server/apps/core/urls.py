from django.urls import include, path

urlpatterns = [
    path('', include('apps.modules.users.urls'), name='users'),
    path('', include('apps.modules.budgets.urls'), name='budgets'),
    path('', include('apps.modules.expenses.urls'), name='expenses'),
]