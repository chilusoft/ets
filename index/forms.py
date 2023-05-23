from django import forms

from index.models import Expense



class ExpenseCreationForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'