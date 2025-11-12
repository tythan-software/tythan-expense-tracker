from django.contrib import admin

from apps.modules.expenses.models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["pk", "owner", "date", "source", "category", "content", "amount"]


admin.site.register(Expense, ExpenseAdmin)
