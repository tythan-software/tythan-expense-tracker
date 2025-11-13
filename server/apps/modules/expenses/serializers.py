from rest_framework import serializers
from apps.common.serializers import LocalizedModelSerializer
from apps.modules.expenses.models import Expense

class ExpenseSerializer(LocalizedModelSerializer):
    # Override the amount formatting in responses
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Expense
        fields = ['id', 'amount', 'content', 'date', 'category']
    
    def get_amount(self, obj):
        return float(obj.amount) if obj.amount is not None else 0.0

    
class ExpenseCreateOrUpdateSerializer(LocalizedModelSerializer):
    class Meta:
        model = Expense
        fields = ['amount', 'content', 'date', 'category']