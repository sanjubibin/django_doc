from rest_framework import serializers
from app1.models import LocationUSADataModel


class LocationUSADataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationUSADataModel
        fields = "__all__"