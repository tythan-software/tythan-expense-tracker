from rest_framework.routers import DefaultRouter
from apps.modules.budgets.views import BudgetViewSet

router = DefaultRouter()
router.register(r'budgets', BudgetViewSet, basename='budgets')
urlpatterns = router.urls
