from django import forms
from django.contrib.auth.forms import UserCreationForm
from index.models import Expense, Investment, Product, User, Quotation, QuotationItem


class ProductForm(forms.ModelForm):
     class Meta:
          model = Product
          fields = '__all__'

class QuotationForm(forms.ModelForm):
    
        class Meta:
            model = Quotation
            fields = '__all__'


class QuotationItemForm(forms.ModelForm):
     class Meta:
          model = QuotationItem
          fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','phone_number','email','password1','password2']

class ExpenseCreationForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'

class InvestmentForm(forms.ModelForm):

    class Meta:
        model = Investment
        exclude = ('actual_return', 'profit')