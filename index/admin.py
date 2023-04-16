from django.contrib import admin

from index.models import Expense, Investment, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')
    search_fields = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'amount', 'description', 'expense_type', 'date_created', 'data_updated')
    search_fields = ('id','user', 'amount', 'description', 'expense_type', 'date_created', 'data_updated')
    list_filter = ('expense_type',)

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'amount', 'expected_return', 'actial_return', 'profit', 'description', 'date_created', 'data_updated')
    search_fields = ('id','user', 'amount', 'expected_return', 'actial_return', 'profit', 'description', 'date_created', 'data_updated')

admin.site.register(User, UserAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Investment, InvestmentAdmin)