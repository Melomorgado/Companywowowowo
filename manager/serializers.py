from rest_framework import serializers
from .models import Manager # manager = class

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'