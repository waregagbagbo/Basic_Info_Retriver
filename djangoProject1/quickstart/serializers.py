from rest_framework import serializers
from .models import UserData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ('email', 'current_datetime','github_url',)