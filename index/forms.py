from django import forms
from django.contrib.auth.forms import UserCreationForm
from index.models import Expense, Investment, User



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