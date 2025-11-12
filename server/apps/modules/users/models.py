"""
Custom user model.
"""

from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    """
    Custom user model extending AbstractUser.
    """
    # Add your custom fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        """
        Meta options for CustomUser.
        """
        db_table = "users"