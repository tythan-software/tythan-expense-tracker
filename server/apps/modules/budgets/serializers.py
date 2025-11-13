from rest_framework import serializers
from apps.common.serializers import LocalizedModelSerializer
from apps.modules.budgets.models import Budget
     
class BudgetSerializer(LocalizedModelSerializer):
    # Override the amount formatting in responses
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ['id', 'amount']

    def get_amount(self, obj):
        return float(obj.amount) if obj.amount is not None else 0.0