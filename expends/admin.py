from django.contrib import admin
from expends import models
# Register your models here.

class BaseAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        qs = qs.filter(owner=request.user)
        return qs

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

class IncomeAdmin(BaseAdmin):
    fields = ("date","source","detail","amount")
    list_display = ("date","amount","source")

    
class ExpendAdmin(BaseAdmin):
    fields = ("date","where","detail","amount")
    list_display = ("date","where","amount")
    
class BillAdmin(BaseAdmin):
    fields = ("detail","duration","cutoff","amount","active")
    list_display = ("cutoff","amount","detail")

    
admin.site.register(models.Income,IncomeAdmin)
admin.site.register(models.Expend,ExpendAdmin)
admin.site.register(models.Bill,BillAdmin)
