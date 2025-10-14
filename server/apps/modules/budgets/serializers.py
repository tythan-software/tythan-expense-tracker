from rest_framework import serializers
from modules.expenses.models import Budget
     
class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'