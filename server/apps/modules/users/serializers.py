from apps.common.serializers import LocalizedModelSerializer
from apps.modules.users.models import User

class UserSerializer(LocalizedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']