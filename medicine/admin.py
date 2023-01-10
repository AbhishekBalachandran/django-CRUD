from django.contrib import admin
from .models import Medicine

# Register your models here.

# class MedicineAdmin(admin.ModelAdmin):
#     list_display = ( 'product_name', 'name_of_manufacturer', 'price', 'description','date_of_manufacture')
#     fields = [ 'product_name', 'price','description' ('name_of_manufacturer', 'date_of_manufacture')]
# # Register the admin class with the associated model
# admin.site.register(Medicine, MedicineAdmin)

admin.site.register(Medicine)