from django.contrib import admin
from users.models import user

class userAdmin(admin.ModelAdmin):
    fieldsets = [
        # ('Info',    {'fields': ['name'], 'fields': ['email'], 'fields': ['password']}),
        ('Info',    {'fields': ['name','email', 'password']}),
        # ('Date information', {'fields': ['pub_date'],'classes': ['collapse']})
    ]

    list_display = ('name', 'email', 'password')
    # list_filter = ['pub_date']
    search_fields = ['name']
    # date_hierarchy = 'pub_date'


admin.site.register(user, userAdmin)