from django.contrib import admin
from .models import Bank, Branch


# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    search_fields = ['ifsc', 'branch', 'bank']
    list_display = ('ifsc','branch','state','city', 'district')

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    