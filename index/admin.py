from django.contrib import admin

from index.models import Customer, Expense, Investment, Product, Quotation, QuotationItem, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')
    search_fields = ('id','first_name', 'last_name', 'username', 'email', 'phone_number')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'amount', 'description', 'expense_type', 'date_created', 'data_updated')
    search_fields = ('id','user', 'amount', 'description', 'expense_type', 'date_created', 'data_updated')
    list_filter = ('expense_type',)

class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'amount', 'expected_return', 'actual_return', 'profit', 'description', 'date_created', 'data_updated')
    search_fields = ('id','user', 'amount', 'expected_return', 'actual_return', 'profit', 'description', 'date_created', 'data_updated')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone')
    search_fields = ('id','name', 'email', 'phone')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'description')
    search_fields = ('id','name', 'price', 'description')

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price','status' ,'date_created', 'date_updated')
    search_fields = ('id', 'total_price','status' ,'date_created', 'date_updated')


class QuotationItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity')
    search_fields = ('id','quotation__id', 'product', 'quantity')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(QuotationItem, QuotationItemAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Investment, InvestmentAdmin)