from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    """
    A serializer (i.e. convert querysets and model instances to Python datatypes or back) that corresponds to the User
    model fields
    """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
