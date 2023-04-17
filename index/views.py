from django.shortcuts import redirect, render
# import get_user_model
from django.contrib.auth import get_user_model as User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def expenses(request):

    if request.user.is_authenticated:
        user = request.user
        expenses = user.expense_set.all()
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
        }
        return render(request, 'index/expenses.html', context)
    else:
        return redirect('login')

def investments(request):
    return render(request, 'index/investments.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()

        return render(request, 'core/register.html', {'form': form})
