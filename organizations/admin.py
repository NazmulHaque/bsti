from django.contrib import admin
from organizations.models import organization

class organInfo(admin.ModelAdmin):
    fieldsets = [
        ('Organization Info',   {'fields': ['name','division','district','thana','address','contact']}),
        # ('Date information', {'fields': ['pub_date'],'classes': ['collapse']})
    ]
    list_display = ('name', 'division', 'district','thana', 'address', 'contact')

    search_fields = ['name']
    # date_hierarchy = 'pub_date'


admin.site.register(organization, organInfo)