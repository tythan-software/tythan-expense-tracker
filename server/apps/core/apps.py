#Django imports
from django.apps import AppConfig

class CoreConfig(AppConfig):
    """
    Core application configuration.
    """
    
    default_auto_field = "django.db.models.AutoField"
    name = "apps.core"