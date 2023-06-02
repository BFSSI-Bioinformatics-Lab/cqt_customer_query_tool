from .models import Query
from rest_framework import serializers

class QuerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Query
        fields = '__all__'