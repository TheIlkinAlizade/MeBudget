from django import forms
from .models import MyModel, User

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname", "birthday",]
    labels = {'fullname': "Name", "birthday": "birthday",}

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = User
    fields = ["username", "password",]
    inputs = {'username': "Name"}

class ExpenseForm(forms.Form):
    product_title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'product-title',
            'placeholder': 'Enter Title of Product'
        })
    )
    user_amount = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'id': 'user-amount',
            'placeholder': 'Enter Cost of Product'
        })
    )