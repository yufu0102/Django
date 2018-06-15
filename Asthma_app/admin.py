from django.contrib import admin
from .models import Information
# Register your models here.

class InformationAdmin(admin.ModelAdmin):
	list_display = ['age', 'gender', 'BH', 'BW', 'smoking', 'allergy', 'IgE', 'rhinosinusitis', 'PFT', 'FVC', 'FEV1', 'PAH']
admin.site.register(Information, InformationAdmin)