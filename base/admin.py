from django.contrib import admin
from django.contrib.auth import get_user_model

from base.models.guards import Guard

from .models import Employee, Car, Visit

User = get_user_model()

class BaseAdminArea(admin.AdminSite):
    site_header = 'Base Database'


class BaseSitePermissions(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'user':
                kwargs["queryset"] = User.objects.filter(username=request.user.username)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


base_site = BaseAdminArea(name='BaseAdmin')

base_site.register(Guard)
base_site.register(Employee, BaseSitePermissions)
base_site.register(Visit, BaseSitePermissions)
base_site.register(Car, BaseSitePermissions)

