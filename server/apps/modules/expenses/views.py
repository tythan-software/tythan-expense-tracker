from django.shortcuts import get_object_or_404

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.core.viewsets import AuthViewSet
from apps.common import utils
from apps.common.permissions import IsOwnerOnly
from apps.common.constants import ExpenseCategory
from apps.modules.expenses.models import Expense
from apps.modules.expenses.serializers import ExpenseSerializer, ExpenseCreateOrUpdateSerializer


@extend_schema(tags=['Expenses'])
class ExpenseViewSet(AuthViewSet):
    """
    API for managing user expenses.
    """
    serializer_class = ExpenseCreateOrUpdateSerializer
    permission_classes_by_action = {
        "get_paginated_expenses": [IsAuthenticated, IsOwnerOnly],
        "line_chart_data": [IsAuthenticated, IsOwnerOnly],
        "expenses_by_month_bar_chart_data": [IsAuthenticated, IsOwnerOnly],
        "expenses_by_week_bar_chart_data": [IsAuthenticated, IsOwnerOnly],
        "total_expenses_pie_chart_data": [IsAuthenticated, IsOwnerOnly],
        "monthly_expenses_pie_chart_data": [IsAuthenticated, IsOwnerOnly],
        "statistics_table_data": [IsAuthenticated, IsOwnerOnly],
    }
    
    def list(self, request):
        """
        API endpoint that allows users to get their expenses.
        """
        expenses = Expense.objects.filter(
            owner=request.user).order_by("-date")
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = ExpenseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category = serializer.validated_data.get('category', None)
        if category and category not in ExpenseCategory.values:
            request.data['category'] = ExpenseCategory.OTHER

        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        
        serializer = ExpenseSerializer(expense, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='expense-categories')
    def get_expense_categories(self, request):
        """
        Returns a list of all available expense categories.
        """
        categories = [
            {"key": category.name, "value": category.value, "label": category.label}
            for category in ExpenseCategory
        ]

        return Response(categories, status=status.HTTP_200_OK
        )

    @extend_schema(
        parameters=[
            OpenApiParameter(name="page", type=OpenApiTypes.INT, required=False),
            OpenApiParameter(name="page_size", type=OpenApiTypes.INT, required=False),
        ],
    )
    @action(detail=False, methods=['get'], url_path='paginated-expenses')
    def get_paginated_expenses(self, request):
        """
        Returns the authenticated user's expenses in a paginated format.
        Supports query params:
        - page: page number
        - page_size: number of items per page (max 100)
        """
        from apps.common.pagination import StandardResultsSetPagination

        expenses = Expense.objects.filter(
            owner=request.user).order_by("-date")

        # Initialize the pagination
        paginator = StandardResultsSetPagination()

        # Gracefully handle page_size override if provided and numeric
        page = request.query_params.get("page")
        page_size = request.query_params.get("page_size")
        if page_size and page_size.isdigit():
            paginator.page_size = min(int(page_size), paginator.max_page_size)
        if page and page.isdigit():
            paginator.page = int(page)

        # Paginate the queryset
        paginated_queryset = paginator.paginate_queryset(expenses, request)

        # Serialize the paginated result
        serializer = ExpenseSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='line-chart-data')
    def line_chart_data(self, request):
        user_expenses = Expense.objects.filter(owner=request.user)
        expenses = user_expenses

        dates = [exp.date for exp in expenses]
        dates = [utils.reformat_date(date, "%d' %b") for date in dates]
        dates.reverse()

        amounts = [round(float(exp.amount), 2) for exp in expenses]
        amounts.reverse()

        chart_data = {}

        for i in range(len(dates)):
            if dates[i] not in chart_data:
                chart_data[dates[i]] = amounts[i]
            else:
                chart_data[dates[i]] += amounts[i]
        return Response(chart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='expenses-by-month-bar-chart-data')
    def expenses_by_month_bar_chart_data(self, request):
        user_expenses = Expense.objects.filter(owner=request.user)
        current_year = utils.get_year_num()
        last_year = current_year - 1

        last_year_month_expenses = utils.get_yearly_month_expense_data(
            last_year, user_expenses
        )
        current_year_month_expenses = utils.get_yearly_month_expense_data(
            current_year, user_expenses
        )
        chart_data = {**last_year_month_expenses, **current_year_month_expenses}
        return Response(chart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='expenses-by-week-bar-chart-data')
    def expenses_by_week_bar_chart_data(self, request):
        weeks = ["current week", "last week", "2 weeks ago", "3 weeks ago"]
        weeks.reverse()

        expenses = [
            Expense.objects.get_weekly_expense_sum(request.user),
            Expense.objects.get_weekly_expense_sum(request.user, -1),
            Expense.objects.get_weekly_expense_sum(request.user, -2),
            Expense.objects.get_weekly_expense_sum(request.user, -3),
        ]
        expenses.reverse()

        chart_data = {}
        for i, week in enumerate(weeks):
            chart_data[week] = expenses[i]
        return Response(chart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='total-expenses-pie-chart-data')
    def total_expenses_pie_chart_data(self, request):
        user_expenses = Expense.objects.filter(owner=request.user)

        chart_data = {}
        for exp in user_expenses:
            if exp.category not in chart_data:
                chart_data[exp.category] = float(exp.amount)
            else:
                chart_data[exp.category] += float(exp.amount)

        for category, amount in chart_data.items():
            chart_data[category] = round(amount, 2)
        return Response(chart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='monthly-expenses-pie-chart-data')
    def monthly_expenses_pie_chart_data(self, request):
        user_expenses = Expense.objects.filter(owner=request.user)

        month_num = utils.get_month_num()
        monthly_expenses = user_expenses.filter(date__month=month_num)

        chart_data = {}
        for exp in monthly_expenses:
            if exp.category not in chart_data:
                chart_data[exp.category] = float(exp.amount)
            else:
                chart_data[exp.category] += float(exp.amount)

        for category, amount in chart_data.items():
            chart_data[category] = round(amount, 2)
        return Response(chart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='statistics-table-data')
    def statistics_table_data(self, request):
        statistics = Expense.objects.get_statistics(request.user)
        stats = {
            "sum_expense":  float(statistics['sum_expense']),
            'max_expense': float(statistics['max_expense'].amount),
            "max_expense_content": statistics['max_expense_content'],
            "min_expense": float(statistics['min_expense'].amount),
            "min_expense_content": statistics['min_expense_content'],
            "biggest_category_expenditure": statistics['biggest_category_expenditure'],
            "smallest_category_expenditure": statistics['smallest_category_expenditure'],
            "monthly_percentage_diff": float(statistics['monthly_percentage_diff']),
            "monthly_expense_average": float(statistics['monthly_expense_average']),
            "daily_expense_average": float(statistics['daily_expense_average']),
            "curr_month_expense_sum": float(statistics['curr_month_expense_sum']),
            "one_month_ago_expense_sum": float(statistics['one_month_ago_expense_sum']),
        }
        return Response(stats, status=status.HTTP_200_OK)
