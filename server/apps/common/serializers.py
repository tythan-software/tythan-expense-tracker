from datetime import datetime, date
from rest_framework import serializers
from django.utils import timezone
import pytz

class LocalizedModelSerializer(serializers.ModelSerializer):
    """
    A reusable serializer base class that:
    - Converts UTC datetimes from DB → local time on output
    - Accepts local (e.g. UTC+7) datetimes and converts them → UTC on input
    - Supports custom date input formats (YYYY-MM-DD or DD-MM-YYYY)
    """

    # Local timezone (you can override per subclass if needed)
    local_tz = pytz.timezone("Asia/Ho_Chi_Minh")

    # Default accepted date formats (optional)
    # Accept input in "DD/MM/YYYY" or "DD/MM/YYYY HH:MM:SS"
    date = serializers.DateTimeField(
        input_formats=["%d/%m/%Y", "%d/%m/%Y %H:%M:%S"],
        default_timezone=pytz.timezone("Asia/Ho_Chi_Minh")  # localize naive input
    )

    def to_representation(self, instance):
        """Convert UTC datetimes from DB → local time for output."""
        data = super().to_representation(instance)

        for field_name, field in self.fields.items():
            value = getattr(instance, field_name, None)

            if isinstance(value, datetime):
                # Convert UTC datetime → local
                local_value = timezone.localtime(value, self.local_tz)
                data[field_name] = local_value.strftime("%d/%m/%Y")

            elif isinstance(value, date):
                # Simple date field (no time)
                data[field_name] = value.strftime("%d/%m/%Y")
        return data
