from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone_number')