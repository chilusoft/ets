from django.shortcuts import redirect, render
# import get_user_model
from django.contrib.auth import get_user_model as User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def expenses(request):
    return render(request, 'index/expenses.html')

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
