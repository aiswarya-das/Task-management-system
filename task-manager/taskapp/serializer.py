from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        error_messages={
            "blank": "Title cannot be empty or just whitespace.",
            "required": "Title is a required field.",
        }
    )

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "created_at",
            "updated_at",
        ]
