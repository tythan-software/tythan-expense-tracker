from rest_framework import serializers
from apps.modules.expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['amount', 'content', 'date', 'category', 'source']