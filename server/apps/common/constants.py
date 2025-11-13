from django.db import models

class ExpenseCategory(models.TextChoices):
    ONLINE_SHOPPING = "Online shopping", "Online shopping"
    ELECTRONICS = "Electronics", "Electronics"
    CLOTHES = "Clothes", "Clothes"
    TRANSPORT = "Transport", "Transport"
    HEALTH = "Health", "Health"
    EDUCATION = "Education", "Education"
    HOUSING = "Housing", "Housing"
    ENTERTAINMENT = "Entertainment", "Entertainment"
    TRAVEL = "Travel", "Travel"
    GIFTS_DONATIONS = "Gifts & Donations", "Gifts & Donations"
    GROCERIES = "Groceries", "Groceries"
    EAT = "Eat", "Eat"
    DRINK_COFFEE = "Drink & Coffee", "Drink & Coffee"
    OTHER = "Other", "Other"