from rest_framework import serializers
from .models import Datamodels

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datamodels
        fields = '__all__' 
