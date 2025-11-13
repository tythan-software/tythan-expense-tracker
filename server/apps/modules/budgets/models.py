from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from apps.common.models import BaseModel

class Budget(BaseModel):
    amount = models.DecimalField(
        default=10,
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.amount)
    
    class Meta:
        """
        Meta options for Budget.
        """
        db_table = "budgets"