from django.contrib import admin
from .models import Query

# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Query, QueryAdmin)