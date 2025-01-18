from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        error_messages={
            "blank": "Name cannot be empty or just whitespace.",
            "required": "Name is a required field.",
        }
    )

    class Meta:
        model = Drink
        fields = ["id", "name", "description"]
