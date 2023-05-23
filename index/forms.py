from django import forms

from index.models import Expense, Investment



class ExpenseCreationForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'

class InvestmentForm(forms.ModelForm):

    class Meta:
        model = Investment
        exclude = ('actual_return', 'profit')