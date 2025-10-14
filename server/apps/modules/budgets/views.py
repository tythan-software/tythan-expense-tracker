from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from modules.budgets.models import Budget
from modules.budgets.serializers import BudgetSerializer

# Create your views here.


@api_view(['GET'])
def get_budget(request):
    budget = Budget.objects.filter(owner=request.user).first()
    if(budget):
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)
    else:
        return Response({'detail': 'Budget not found'},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_budget(request):
    budget_data = {
        'amount': request.data['amount'],
        'owner': request.user.pk
    }

    serializer = BudgetSerializer(data=budget_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    budget_data = {
        'owner': request.user.pk,
        'amount': request.data['amount'],
    }
    serializer = BudgetSerializer(budget, data=budget_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    budget.delete()
    return Response({'detail': 'Budget deleted successfully'},
                    status=status.HTTP_204_NO_CONTENT)