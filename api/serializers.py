from .models import Query, UserActivity
from rest_framework import serializers


class QuerySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    evaluator = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Query
        fields = '__all__'
        
class UserActivitySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = UserActivity
        fields = '__all__'