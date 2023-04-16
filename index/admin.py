from django.contrib import admin

from index.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')
    search_fields = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')

admin.site.register(User, UserAdmin)