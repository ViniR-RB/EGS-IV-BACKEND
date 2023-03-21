from rest_framework import serializers

from .models import *


class TodoSerializer(serializers.Serializer):
    class Meta:
        model = TodoModel
        fields = '__all__'
