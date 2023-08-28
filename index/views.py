from datetime import datetime
from django.shortcuts import redirect, render
# import get_user_model
from django.contrib.auth import get_user_model as User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
from django.views import View
from django.http import HttpResponse

from index.models import Expense, Quotation

from .forms import ExpenseCreationForm, InvestmentForm, ProductForm, QuotationForm, QuotationItemForm, UserRegisterForm
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

@login_required
def expenses(request):

    expense_creation_form = ExpenseCreationForm()
    expense_creation_form.fields['user'].initial = request.user
    # disable the user field
    expense_creation_form.fields['user'].widget.attrs['disabled'] = True
    if request.user.is_authenticated:
        user = request.user
        expenses = Expense.objects.filter(user=user)
        if request.method == 'POST':
            try:
                expense_creation_form = ExpenseCreationForm(data=request.POST)
                expense_creation_form.fields['user'].initial = request.user

                if expense_creation_form.is_valid():
                    expense_creation_form.save()
                    return redirect('index:expenses')
            except Exception as e:
                return HttpResponse(e)
        # Get total for expense type, Food
        else:
            ...
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


@login_required
def investments(request):
    if request.method != 'POST':
        month_pack = []
        capt_inv_pack = []
        expected_return_pack = []
        actual_return_pack = []
        for i in range(1, 13):

            month_start = f'2020-{i}-01'
            # AGGREGATE SUM OF INVESTMENTS per month
            month_investments = request.user.investment_set.filter(date_created__month=i).aggregate(Sum('amount')).get('amount__sum') if not None else 0
            month_expected_return = request.user.investment_set.filter(date_created__month=i).aggregate(Sum('expected_return')).get('expected_return__sum') if not None else 0
            month_actual_return = request.user.investment_set.filter(date_created__month=i).aggregate(Sum('actual_return')).get('actual_return__sum') if not None else 0
            print(month_investments)
            # print(month_investments)
           
            capt_inv_pack.append(month_investments)
            expected_return_pack.append(month_expected_return)
            actual_return_pack.append(month_actual_return)

            month_start = datetime.strptime(month_start, '%Y-%m-%d')
            month_pack.append(month_start.strftime('%B'))
        print(capt_inv_pack)
        print(expected_return_pack)
        print(actual_return_pack)
        initial_data = {
            'user': request.user,
        }
        inv_form = InvestmentForm(initial=initial_data)
        return render(request, 'index/investments.html',
                       {'inv_form': inv_form,
                         'month_pack': month_pack, 
                        'capt_inv_pack': capt_inv_pack,
                        'act_ret_pack': actual_return_pack,
                        'exp_ret_pack': expected_return_pack,})
    else:
        inv_form = InvestmentForm(request.POST)
        inv_form.fields['user'].initial = request.user
        if inv_form.is_valid():
            inv_form.save()
            return redirect('index:investments')
        else:
            # return redirect('index:investments')
            return render(request, 'index/investments.html', {'inv_form': inv_form})

@login_required
def business(request):
    quotations = Quotation.objects.all()
    quote_form = QuotationForm()
    quote_item_form = QuotationItemForm()
    product_form = ProductForm()
    ctx = {'quotations': quotations, 'quote_form': quote_form, 'quote_item_form': quote_item_form, 'product_form': product_form}
    return render(request, 'index/business.html', ctx)


def create_quote(request):
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:business')
    else:
        form = QuotationForm()

    return render(request, 'index/business.html', {'quote_form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return render(request, 'index/index.html')
    else:
        form = UserRegisterForm()

        return render(request, 'core/register.html', {'form': form})
