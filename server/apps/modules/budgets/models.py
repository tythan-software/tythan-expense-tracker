from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import BaseModel

# Create your models here.

class BudgetManager(models.Manager):
    def get_budget(self, owner):
        budget = Budget.objects.filter(owner=owner).first()
        return budget.amount if budget else 0
    
    def delete_testuser_budget(self, request):
        if str(request.user) == "testuser1" or str(request.user) == "testuser3":
            test_user_budget = Budget.objects.all()
            test_user_budget.delete()


class Budget(BaseModel):
    amount = models.DecimalField(
        default=10,
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = BudgetManager()

    def __str__(self):
        return str(self.amount)
    
    class Meta:
        """
        Meta options for Budget.
        """
        
        db_table = "budgets"