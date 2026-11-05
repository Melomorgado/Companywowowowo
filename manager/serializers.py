from rest_framework import serializers
from .models import Manager # manager = class


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
         # JSON format ng DATA
        # QuerySet <- not readable by others
        # QuerySet - > JSON
        # JSON - > QuerySet