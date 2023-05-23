from django.shortcuts import redirect, render
# import get_user_model
from django.contrib.auth import get_user_model as User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum

from .forms import ExpenseCreationForm, InvestmentForm
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def expenses(request):

    expense_creation_form = ExpenseCreationForm()
    expense_creation_form.fields['user'].initial = request.user
    # disable the user field
    expense_creation_form.fields['user'].widget.attrs['disabled'] = True
    if request.user.is_authenticated:
        user = request.user
        expenses = user.expense_set.all()
        if request.method == 'POST':
            form = ExpenseCreationForm(request.POST)
            form.fields['user'].initial = request.user

            if form.is_valid():
                form.save()
                return redirect('index:expenses')
       
        # Get total for expense type, Food
        exp_lst = []
        def check_if_none(value):
            if value is None:
                return 0
            else:
                return value
            
        all_expense_total = expenses.aggregate(Sum('amount'))
        all_food_expenses = expenses.filter(expense_type='Food').aggregate(Sum('amount'))
        all_travel_expenses = expenses.filter(expense_type='Travel').aggregate(Sum('amount'))
        all_entertainment_expenses = expenses.filter(expense_type='Entertainment').aggregate(Sum('amount'))
        all_internet_expenses = expenses.filter(expense_type='Internet').aggregate(Sum('amount'))
        all_other_expenses = expenses.filter(expense_type='Other').aggregate(Sum('amount')) 

        all_expense_total['amount__sum'] = check_if_none(all_expense_total['amount__sum'])
        all_food_expenses['amount__sum'] = check_if_none(all_food_expenses['amount__sum'])
        all_travel_expenses['amount__sum'] = check_if_none(all_travel_expenses['amount__sum'])
        all_entertainment_expenses['amount__sum'] = check_if_none(all_entertainment_expenses['amount__sum'])
        all_internet_expenses['amount__sum'] = check_if_none(all_internet_expenses['amount__sum'])
        all_other_expenses['amount__sum'] = check_if_none(all_other_expenses['amount__sum'])


        context = {
            'expenses': expenses,
            'all_expense_total': all_expense_total.get('amount__sum'),
            'all_food_expenses': all_food_expenses.get('amount__sum'),
            'all_travel_expenses': all_travel_expenses.get('amount__sum'),
            'all_entertainment_expenses': all_entertainment_expenses.get('amount__sum'),
            'all_internet_expenses': all_internet_expenses.get('amount__sum'),
            'all_other_expenses': all_other_expenses.get('amount__sum'),
            'expense_creation_form': expense_creation_form,
        }
        return render(request, 'index/expenses.html', context)
    else:
        return redirect('login')

def investments(request):
    if request.method != 'POST':
        inv_form = InvestmentForm()
        inv_form.fields['user'].initial = request.user
        inv_form.fields['user'].widget.attrs['disabled'] = True
        inv_form.fields['amount'].widget.attrs['placeholder'] = 'Amount in Kwacha'
        inv_form.fields['amount'].widget.attrs['step'] = 0.01
        return render(request, 'index/investments.html', {'inv_form': inv_form})
    else:
        inv_form = InvestmentForm(request.POST)
        inv_form.fields['user'].initial = request.user
        inv_form.fields['user'].widget.attrs['disabled'] = True
        if inv_form.is_valid():
            inv_form.save()
            return redirect('index:investments')
        else:
            return redirect('index:investments')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()

        return render(request, 'core/register.html', {'form': form})
