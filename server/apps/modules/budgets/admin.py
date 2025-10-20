from django.contrib import admin

from apps.modules.budgets.models import Budget

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ["pk", "owner", "amount"]

admin.site.register(Budget, BudgetAdmin)
