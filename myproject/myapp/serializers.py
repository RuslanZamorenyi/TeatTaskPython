from rest_framework import serializers

from .models import CostsModel


class CostsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostsModel
        fields = '__all__'
