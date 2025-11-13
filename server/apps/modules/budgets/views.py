from django.shortcuts import get_object_or_404

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from apps.modules.budgets.models import Budget
from apps.modules.budgets.serializers import BudgetSerializer
from apps.core.viewsets import AuthViewSet

@extend_schema(tags=['Budgets'])
class BudgetViewSet(AuthViewSet):
    """
    API for managing budgets.
    """
    serializer_class = BudgetSerializer
    
    def list(self, request):
        budget = Budget.objects.filter(owner=request.user)
        serializer = BudgetSerializer(budget, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        amount = request.data.get('amount', None)
        if amount is None:
            raise ParseError(detail="Missing required field: 'amount'.")

        serializer = BudgetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)

        amount = request.data.get('amount')
        if amount is None:
            raise ParseError("Missing required field: 'amount'.")

        serializer = BudgetSerializer(budget, request.data, partial=False)

        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        budget = get_object_or_404(Budget, pk=pk)

        budget.delete(owner=request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)
