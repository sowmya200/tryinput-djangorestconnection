from rest_framework import serializers
from .models import UserInput

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['user_input']
