from django.db.models import fields
from rest_framework import serializers

from . import models

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Search
        fields = "__all__"