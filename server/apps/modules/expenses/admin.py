from django.contrib import admin

from apps.modules.expenses.models import Expense

# Register your models here.


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["pk", "owner", "date", "source", "category", "content", "amount"]

admin.site.register(Expense, ExpenseAdmin)
