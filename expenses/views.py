from django.shortcuts import render,redirect
from . models import MyExpenses
from django.contrib import messages
# Create your views here.
def add_expense(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        date = request.POST.get('date')
        description = request.POST.get('description')
        
        new_expenses = MyExpenses(
            amount = amount,
            category = category,
            date = date,
            description = description
        )
        
        new_expenses.save()
        messages.success(request , "expenses added successfully")
        
        return redirect ('add_expense')
    return render(request, 'home.html')