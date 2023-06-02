from django.shortcuts import render
from rest_framework import viewsets


from .models import Query
from .serializers import QuerySerializer


class QueryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Query.objects.all().order_by('id')
    serializer_class = QuerySerializer

# Create your views here.
