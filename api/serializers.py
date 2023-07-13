from .models import Query
from rest_framework import serializers


class QuerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    evaluator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Query
        fields = '__all__'