from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Clears all data from Expense table"

    def handle(self, *args, **kwargs):
        from apps.modules.expenses.models import Expense
        Expense.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All expenses deleted."))
