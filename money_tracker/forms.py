from django import forms
from django.forms import ModelForm

from .models import Expense

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name','category','amount','date']
        excluse = ["user"]
        widgets = {
            "expense_name":	forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "amount": forms.TextInput(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={'class': 'form-control','type':'date'})
        }
