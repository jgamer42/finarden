from django.contrib import admin
from tips.models import Tip
from tips.views import ModifyIndex

# Register your models here.
class TipAdmin(admin.ModelAdmin):
    list_display = ("created","detail","active")
    list_editable = ("active",)

admin.site.register(Tip,TipAdmin)
admin.site.index = ModifyIndex(admin.site.index).target_index