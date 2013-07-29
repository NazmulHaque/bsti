from django.contrib import admin
from products.models import product

class productInfo(admin.ModelAdmin):
    fieldsets = [
        ('Product Info',    {'fields': ['type','brand','organization','license_no','issue_date','expire_date']}),
    ]
    list_display = ('type','brand','organization','license_no','issue_date','expire_date')

    search_fields = ['type']
    # date_hierarchy = 'pub_date'


admin.site.register(product, productInfo)