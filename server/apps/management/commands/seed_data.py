from django.core.management.base import BaseCommand
from apps.modules.users.models import User
from apps.common import utils

class Command(BaseCommand):
    help = "Seed initial data"

    def handle(self, *args, **kwargs):
        user = User.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR("❌ No users found. Please create a user first."))
            return

        # Load expense data

        try:
            expenses_by_date = utils.get_data_from_json(
                "apps/management/data/initial_data.json"
            )
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("❌ JSON data file not found."))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Failed to load JSON: {e}"))
            return

        # Generate and seed expenses
        try:
            expense_generator = utils.ExpenseGenerator(expenses_by_date)
            expenses = expense_generator.generate_expenses()

            if not expenses:
                self.stdout.write(self.style.WARNING("⚠️ No expenses generated."))
                return

            from apps.modules.expenses.models import Expense
            Expense.objects.bulk_create([
                Expense(
                    amount=e["amount"],
                    content=e["content"],
                    category=e["category"],
                    source=e["source"],
                    owner=user,
                )
                for e in expenses
            ])

            self.stdout.write(self.style.SUCCESS(f"✅ Successfully seeded {len(expenses)                } expenses!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error while seeding expenses: {e}"))
