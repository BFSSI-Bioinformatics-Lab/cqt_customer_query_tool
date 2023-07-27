from django.contrib import admin
from .models import Query, UserActivity

# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Query, QueryAdmin)

class UserActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserActivity, UserActivityAdmin)