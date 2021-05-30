from rest_framework import serializers
from .models import Empmodels


class CRUD_serialize(serializers.ModelSerializer):
    class Meta:
        model = Empmodels
        fields = "__all__"
